# FRED API Key Setup

This analysis requires a free FRED (Federal Reserve Economic Data) API key to download macroeconomic data.

## Getting Your API Key

1. Visit: https://fred.stlouisfed.org/docs/api/api_key.html
2. Register for a free account (if you don't have one)
3. Create an API key (it's free and takes ~1 minute)
4. Copy your API key

## Setting Your API Key

### Option 1: For Current Session Only
```bash
export FRED_API_KEY='your_key_here'
```

### Option 2: Permanent (Recommended)
Add to your shell configuration file:

**For bash (~/.bashrc):**
```bash
echo "export FRED_API_KEY='your_key_here'" >> ~/.bashrc
source ~/.bashrc
```

**For zsh (~/.zshrc):**
```bash
echo "export FRED_API_KEY='your_key_here'" >> ~/.zshrc
source ~/.zshrc
```

### Option 3: Use the Reproduce Script
The `reproduce.sh` script will prompt you for your API key if it's not set.

## Verifying Your Key

Test that your key works:
```bash
python3 -c "from fredapi import Fred; fred = Fred(api_key='$FRED_API_KEY'); print('✓ API key works!')"
```

## Security Note

**Never commit your API key to git!** The notebook will prompt you to set it as an environment variable, which keeps it out of the code.
