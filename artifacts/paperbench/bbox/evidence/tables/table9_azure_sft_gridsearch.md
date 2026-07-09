# Table 9: Azure-SFT Grid Search on GSM8K
- **Source**: Table 9, Appendix F.3
- **Caption**: "Simple grid search for Azure-SFT on GSM8K dataset."
- **Conditions**: Azure OpenAI GPT-3.5-turbo fine-tuning API; GSM8K dataset; 3 trials due to budget constraints (~$200 per trial); only 3 hyperparameters adjustable (epochs, batch size, LR multiplier)

| # Training Epochs | Batch Size | Learning Rate Multiplier | Accuracy |
|-------------------|------------|--------------------------|----------|
| (Not specified) | (Not specified) | (Not specified) | 67.82 |
| (Not specified) | (Not specified) | (Not specified) | 69.94 |
| (Not specified) | (Not specified) | (Not specified) | 66.71 |

**Note**: The paper does not report the specific epoch/batch/LR values for each trial, only the accuracy outcomes. All three trials show limited variation, demonstrating the opacity of the Azure-SFT API. Budget: ~$200 per trial.
