letter = '''Dear <|NAME|>,
            You are selected!
            Date : <|DATE|>
            Thanks and Regards,
            Pritom'''
print(letter.replace("<|NAME|>", "Pritom").replace("<|DATE|>", "20th June 2024"))