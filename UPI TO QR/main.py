import qrcode

def generate_upi_qr(upi_id, amount, filename="upi_qr.png"):
    """
    Generate QR code for UPI payment
    
    Args:
        upi_id (str): UPI ID (e.g., "user@paytm")
        amount (float): Payment amount
        filename (str): Output filename
    """
    
    # Create UPI URL
    upi_url = f"upi://pay?pa={upi_id}&am={amount}&cu=INR"
    
    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(upi_url)
    qr.make(fit=True)
    
    # Create and save image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    
    print(f"QR code saved as {filename}")

# User input
if __name__ == "__main__":
    upi_id = input("Enter UPI ID: ")
    amount = float(input("Enter amount: "))
    filename = input("Enter filename (or press Enter for 'upi_qr.png'): ")
    
    if not filename:
        filename = "upi_qr.png"
    
    generate_upi_qr(upi_id, amount, filename)