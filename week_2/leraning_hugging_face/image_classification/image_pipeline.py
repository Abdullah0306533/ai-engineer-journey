import numpy as np
from datasets import load_dataset
from transformers import AutoModelForImageClassification, TrainingArguments,Trainer
from pygments.formatters import img
import evaluate
from transformers import DefaultDataCollator
from transformers import AutoImageProcessor
from torchvision.transforms import RandomResizedCrop, Compose, Normalize, ToTensor

# Loading the training data
food = load_dataset("ethz/food101", split="train[:5000]")
# Dividing the data
food = food.train_test_split(test_size=0.2)

# Creating dictionaries tho help model assigning an integer number to the respected label

labels = food["train"].features["label"].names
label2id, id2label = dict(), dict()
for i, label in enumerate(labels):
    label2id[label] = str(i)
    id2label[str(i)] = label
# Loading a ViT image processor
checkpoint = "google/vit-base-patch16-224-in21k"
image_processor = AutoImageProcessor.from_pretrained(checkpoint)

# Applying transformations
normalize = Normalize(mean=image_processor.image_mean, std=image_processor.image_std)
size = (image_processor.size["shortest_edge"]
        if "shortest_edge" in image_processor.size
        else (image_processor.size["height"], image_processor.size["width"])
        )
_transforms = Compose([RandomResizedCrop(size), ToTensor(), normalize])


# create a preprocessing function to apply the transforms and return the pixel_values
def transform(examples):
    examples["pixel_values"] = [_transforms(img.convert("RGB")) for img in examples["image"]]
    del examples["image"]
    return examples


food = food.with_transform(transform)
data_collator = DefaultDataCollator()
accuracy = evaluate.load("accuracy")


# Computing Accuracy
def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return accuracy.compute(predictions=predictions, labels=labels)


# Creating Model
model=AutoModelForImageClassification.from_pretrained(
    checkpoint,
    num_labels=len(labels),
    id2label=id2label,
    label2id=label2id,
)
# Fine-Tuning Model
training_args = TrainingArguments(
    output_dir="model_fine_tuning",
    remove_unused_columns=False,
    eval_strategy="epoch",
    save_strategy="epoch",
    learning_rate=5e-5,
    per_device_train_batch_size=16,
    gradient_accumulation_steps=4,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    warmup_steps=0.1,
    logging_steps=10,
    report_to="trackio",
    run_name="food101",
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    push_to_hub=False,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=food["train"],
    eval_dataset=food["test"],
    processing_class=image_processor,
    compute_metrics=compute_metrics,
)

trainer.train()

ds = load_dataset("ethz/food101", split="validation[:10]")
image = ds["image"][0]