# 🕵️‍♂️ Image Steganography with Python  

## 📖 Overview  

This project demonstrates **image steganography**, a technique used to hide information within an image file. Using **Python**, the project encodes secret messages within an image by manipulating pixel values while preserving the visual integrity of the image.  

The repository includes:  
- A **steganography script (`stegano1.py`)** that performs encoding and decoding.  
- **An image (`aliceStego.jpeg`)** containing hidden data.  
- **A result file (`result.pdf`)** that might reveal extracted information.  

---

## 🛠 Technologies Used  

- **Python** – Core implementation language.  
- **OpenCV** – For image manipulation and processing.  
- **PIL (Pillow)** – Used to modify image pixels.  
- **NumPy** – For handling image arrays efficiently.  

---

## 📌 Features  

✅ **Hide messages inside images** – Encodes text within image pixels.  
✅ **Extract hidden messages** – Retrieves secret information from an image.  
✅ **Lossless Steganography** – The image remains visually unchanged.  
✅ **JPEG and PNG support** – Works with different image formats.  

---

## 📂 Project Structure  

```
📁 Image-Steganography/
│── stegano1.py        # Python script for encoding/decoding messages
│── aliceStego.jpeg    # Image containing a hidden message
│── result.pdf         # Decoded output from the hidden data
│── README.md          # Project documentation
```

---

## 🚀 How It Works  

### **1️⃣ Encode a Message into an Image**  
```sh
python stegano1.py --encode --input original.jpg --output aliceStego.jpeg --message "Secret Message Here"
```

### **2️⃣ Decode the Hidden Message from an Image**  
```sh
python stegano1.py --decode --input aliceStego.jpeg
```

This will extract and display the hidden message from the image.

---

## 🔐 Security Considerations  

- **Steganalysis Detection** – The hidden message can be detected using statistical analysis if poorly implemented.  
- **Data Limitations** – The size of the hidden message is limited by the image's pixel count.  
- **Encryption Integration** – For added security, encryption should be used before embedding text.  

---

## 🔮 Future Enhancements  

🔹 **Support for Audio & Video Steganography** – Extending beyond images.  
🔹 **Advanced Encoding Algorithms** – Using LSB+ or frequency-based techniques.  
🔹 **GUI for Ease of Use** – A simple UI to encode and decode messages.  

---

## 📜 References  

- [Python Pillow Documentation](https://pillow.readthedocs.io/)  
- [OpenCV Python Tutorials](https://docs.opencv.org/)  
- [Steganography Concepts](https://en.wikipedia.org/wiki/Steganography)  

---

## 📧 Contact  

**Author:** Siddartha Reddy Boreddy  
📍 **SUNY Binghamton**  
✉️ **Email:** sboreddy@binghamton.edu  

---

### ⭐ If you find this project helpful, feel free to star the repository! 🚀  
