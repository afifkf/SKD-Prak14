# -*- coding: utf-8 -*-
"""

@author: Afif Khalid Fadhillah
"""

import cv2
import numpy as np

demo = cv2.imread("E:\Semester 3\Sistem Keamanan Data smt 3\SKD 14\WhatsApp Image 2024-01-08 at 13.26.24_af2f5321.jpg", 0)
r, c = demo.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)  # Generate random key image
cv2.imwrite("E:\Semester 3\Sistem Keamanan Data smt 3\SKD 14\key.jpg", key)   # Save key image

cv2.imshow("demo", demo)  # Display original image
cv2.imshow("key", key)  # Display key image

encryption = cv2.bitwise_xor(demo, key)  # encryption
cv2.imwrite("E:\Semester 3\Sistem Keamanan Data smt 3\SKD 14\enkripsiafif.jpg", encryption)     # Save the encrypted image
decryption = cv2.bitwise_xor(encryption, key)  # decrypt
cv2.imwrite("E:\Semester 3\Sistem Keamanan Data smt 3\SKD 14\deskripsiafif.jpg", decryption) # Save the decrypted image

cv2.imshow("encryption", encryption)  # Display ciphertext image
cv2.imshow("decryption", decryption)  # Displays the decrypted image

cv2.waitKey(-1)
cv2.destroyAllWindows()