# UPI QR Code Generator 💳📲

A simple Python script to generate a **UPI payment QR code** that can be scanned to pay directly from any UPI-enabled app.  

---

## Features

- Generate QR code for any **UPI ID**.
- Supports custom **payment amount**.
- Save QR code as an image file.
- Easy to use via terminal input.

---

## Requirements

- Python 3.x
- `qrcode` library
- `Pillow` library (for image generation)

Install dependencies using pip:

```bash
pip install qrcode
pip install pillow
```


## Usage

```bash
python upi_qr_generator.py
```

Then follow the prompts:

```
Enter UPI ID: user@paytm
Enter amount: 150
Enter filename (or press Enter for 'upi_qr.png'):
```

The QR code will be saved to the specified filename (default is `upi_qr.png`).

---

## Example

* **UPI ID:** `ujjwal@okaxis`
* **Amount:** `250`
* **Generated file:** `upi_qr.png`

Scan the QR code with any UPI app to make the payment.

---

## How it Works

The script generates a UPI URL in the format:

```
upi://pay?pa=<UPI_ID>&am=<Amount>&cu=INR
```

This URL is encoded into a QR code using the `qrcode` library and saved as an image.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

## 📄 License

This project is licensed under the MIT License.

<br>

---

<h3 align="center">
  <b>Happy Coding 👨‍💻 | Keep Practicing 💡</b>
</h3>

---

<h3 align="center">
  <b>Let's Connect!! </b>
  <img src="https://user-images.githubusercontent.com/74038190/214644145-264f4759-7633-441e-9d67-d8dda9d50d26.gif" width=95px>
</h3>

<p align="center">
  <a href="https://ujjwal-kamila.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-Visit-blue?logo=Firefox&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/ujjwal-kamila-8a12a4262/"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white"></a>
  <a href="https://leetcode.com/ujjwalkamila86/"><img src="https://img.shields.io/badge/LeetCode-FFA116.svg?logo=LeetCode&logoColor=black"></a>
</p>


