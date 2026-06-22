## MQR-LLM-Thesis

Files for my masters thesis at UCOL. I fine-tuned LLaMA-3.2-3B-Instruct and Qwen2.5-3B-Instruct on medical datasets using LoRA and full instruction tuning to see if smaller models could get better at medical quantitative reasoning.

## What I did
- Fine-tuned both models using LoRA and full instruction tuning on MedInstruct and Med-MathInstruct.
- Med-MathInstruct includes 15% MQR data from MedCalc-Bench-v1.0 to see if it made a difference.
- Evaluated across MedCalc-Bench-v1.0, MedQA-USMLE-4-options, and a MedInstruct test set.

## What I found
- Full instruction tuning was stronger under direct prompting.
- LoRA actually beat GPT-3.5 on MedCalc-Bench under CoT (25.41% vs 23.69%).
- The additional MQR data improved performance on MedCalc-Bench, but had little effect on the other benchmarks.
- Fine-tuning hurt MedQA performance in most cases.
- Full fine-tuning was faster than LoRA in 7/8 cases which was unexpected.
