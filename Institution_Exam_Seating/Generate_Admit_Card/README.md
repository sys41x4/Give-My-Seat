# Give-My-Seat
## [Generate Admit Card]
---

### Script Usage

```
python3 app.py <confirmed_seating_data.json_File_Path> <Institute_Name>
```

### Web App Usage

After Entering `Roll Number` and `Aadhar Number`
click on `Show Admit Card` Button.

Wait for a bit, if everything went well then a Admit Card will be generated for preview.
Then Click on `Download Admit Card` to download the Admit Card as PDF Format


### Web App Preview

[screenshot1](sample_images/generate_admit_card_webapp_screenshot1.png)
[screenshot2](sample_images/generate_admit_card_webapp_screenshot2.png)

### Error Fixing
If you do fix any error regarding `wkhtmltopdf` error
Please do use https://wkhtmltopdf.org/ to download
and refer the `wkhtmltopdf` binary in the `app.py` script
