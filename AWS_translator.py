

import boto3

def perform_translation(text, source_lang='en', target_lang='hi'):
    # Replace 'AWS_ACCESS_KEY' and 'AWS_SECRET_KEY' with your actual AWS credentials
    aws_access_key = 'AWS_ACCESS_KEY'
    aws_secret_key = 'AWS_SECRET_KEY'
    
    translate = boto3.client('translate', aws_access_key_id=aws_access_key,
                             aws_secret_access_key=aws_secret_key,
                             region_name='ap-south-1')

    response = translate.translate_text(
        Text=text,
        SourceLanguageCode=source_lang,
        TargetLanguageCode=target_lang
    )

    return response['TranslatedText']

if __name__ == "__main__":
    # Replace 'Your text here' with the text you want to translate
    text_to_translate = 'Your text here'
    
    # Perform translation
    translated_text = perform_translation(text_to_translate)

    # Print the translated text
    print(f"Translated Text: {translated_text}")
