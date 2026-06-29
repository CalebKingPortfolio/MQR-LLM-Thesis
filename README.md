## MQR-LLM-Thesis
Files from my master's thesis at UCOL. I fine-tuned LLaMA-3.2-3B-Instruct and Qwen2.5-3B-Instruct on medical datasets using LoRA and full instruction tuning to investigate whether smaller models could improve at medical quantitative reasoning.

## What I did
- Fine-tuned both models using LoRA and full instruction tuning on two custom training datasets, MedInstruct and Med-MathInstruct.
- Med-MathInstruct augments MedInstruct with MQR examples from MedCalc-Bench-v1.0 to assess whether the additional data made a difference.
- Evaluated all fine-tuned variants and base models across MedCalc-Bench-v1.0, MedQA-USMLE-4-options, and a custom MedInstruct test set.

## What I found
- Full instruction tuning was the stronger method under direct prompting, beating LoRA in 3 out of 4 variants on MedCalc-Bench-v1.0.
- LLaMA-Med+Math (LoRA) beat GPT-3.5 on MedCalc-Bench under CoT prompting (25.41% vs 23.69%).
- The additional MQR data consistently improved performance on MedCalc-Bench-v1.0 but had little effect on the secondary benchmarks.
- Fine-tuning hurt MedQA-USMLE performance in 6 out of 8 variants.
- Full instruction tuning was faster than LoRA in 7 out of 8 variants, which was completely unexpected.

## Models
All eight fine-tuned model variants are available on Hugging Face under [calebking](https://huggingface.co/calebking).

## Code
The full experiment code including preprocessing scripts, fine-tuning pipelines, and evaluation scripts is available in this repository.
