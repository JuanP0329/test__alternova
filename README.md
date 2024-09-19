# Alternova Test

## Description

This Python script monitors the prices of Bitcoin, Ethereum, and Binance Coin. It automatically sends alerts via WhatsApp using Twilio when the value of any cryptocurrency exceeds a specific threshold.

## Features

- Fetches current cryptocurrency prices using the CoinGecko API.
- Sends WhatsApp alerts when prices exceed defined thresholds.

## Requirements

- Python 3.6 or higher.
- pip (package manager).
- Libraries:
    - `requests`
    - `twilio`

### Create a Virtual Environment

1. Open the terminal and navigate to your project folder:
    ![image1.png](readmeresource%2Fimage1.png)
    
2. Once in the folder, run the following commands to install, create, and activate the virtual environment:
    - Install virtualenv:
        
        ```bash
        pip install virtualenv
        ```
        
    - Create the virtual environment folder:
        
        ```bash
        virtualenv venv
        ```
        
    - Activate the virtual environment:
        
        ```bash
        .\venv\Scripts\activate
        ```
        

### Installing Dependencies

To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
```

## Configuration

### Twilio Account

1. Sign up for Twilio at this [link](https://pages.twilio.com/twilio-brand-sales-spa-latam-2?utm_source=google&utm_medium=cpc&utm_term=twilio&utm_campaign=G_S_LATAM_Brand_Twilio_Spanish&cq_plac=&cq_net=g&cq_pos=&cq_med=&cq_plt=gp&gad_source=1&gclid=EAIaIQobChMIsPfhh-DNiAMVJZ1aBR36rhb1EAAYASAAEgI7WPD_BwE).
2. Click on the "Get Started Free" button.
    ![image2.png](readmeresource%2Fimage2.png)
    
3. Complete your registration with a Google account or by using another email.
    - **Option 1**: Email.
        ![image3.png](readmeresource%2Fimage3.png)
        
    - **Option 2**: With Google.
        ![image4.png](readmeresource%2Fimage4.png)
        
4. Verify your phone number to receive WhatsApp messages.
    ![image5.png](readmeresource%2Fimage5.png)
        
5. Fill in the requested fields and click "Continue."
    ![image6.png](readmeresource%2Fimage6.png)
    
6. Complete the setup by selecting the corresponding fields and click "Get Started with Twilio."
    ![image7.png](readmeresource%2Fimage7.png)
    

### Enable WhatsApp on Twilio

1. Follow the instructions in Twilio's official documentation to enable WhatsApp.
    ![image8.png](readmeresource%2Fimage8.png)
    
2. Link Twilio with your WhatsApp by scanning the QR code or using the provided WhatsApp number (`whatsapp:+14155238886`).
    ![image9.jpg](readmeresource%2Fimage9.jpg)
    
3. Once linked, access the Twilio dashboard.
    ![image10.png](readmeresource%2Fimage10.png)
    
4. Obtain your `Account SID` and `Auth Token` from the Dashboard.
    - In the top left, select "Twilio Home."
        ![image11.png](readmeresource%2Fimage11.png)
        
    - Select your account name.
        ![image12.png](readmeresource%2Fimage12.png)
        
    - On the next screen, you will find both your `Account SID` and `Auth Token`.
        ![image13.png](readmeresource%2Fimage13.png)
        

### Script Setup

- Replace `twilio_account_sid` and `twilio_auth_token` in the code with your Twilio credentials.
    ![image14.png](readmeresource%2Fimage14.png)
    
- Change `your_whatsapp_number` to your WhatsApp number in the format `whatsapp:+<country_code><number>`.
    ![image15.png](readmeresource%2Fimage15.png)
    

## Code Structure

### Functions

- **`get_crypto_price()`**
    - **Description**: Retrieves current prices for Bitcoin, Ethereum, and Binance Coin from CoinGecko.
    - **Return**: A dictionary with cryptocurrency prices.
- **`check_price_and_alert(prices)`**
    - **Description**: Checks if prices exceed the thresholds and sends alerts if necessary.
    - **Parameters**: `prices` — A dictionary with cryptocurrency prices.
- **`send_whatsapp_alert(name, threshold, price)`**
    - **Description**: Sends an alert via WhatsApp.
    - **Parameters**:
        - `name` — Name of the cryptocurrency.
        - `threshold` — Price threshold.
        - `price` — Current price.
- **`main()`**
    - **Description**: Main function that coordinates fetching prices and checking alerts.

## Running the Script

To run the script, use the following command in the terminal:

```bash
python main.py
```

## Customization

You can modify the price thresholds by changing the values in the `thresholds` dictionary inside the `check_price_and_alert` function. Default thresholds:

- **Bitcoin**: $30,000
- **Ethereum**: $2,000
- **Binance Coin**: $300

## Notes

- Make sure your WhatsApp number is verified in Twilio.
- Be aware of potential costs for sending.