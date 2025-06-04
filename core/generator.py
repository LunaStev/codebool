from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "tiiuae/falcon-rw-1b"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

def generate_code(prompt: str, lang: str = "python") -> str:
    full_prompt = f"Write a {lang} function:\n{prompt}\n"

    inputs = tokenizer(full_prompt, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=300,
        do_sample=True,
        temperature=0.7,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id,
    )
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    if full_prompt in generated_text:
        generated_text = generated_text.split(full_prompt)[-1].strip()

    return generated_text