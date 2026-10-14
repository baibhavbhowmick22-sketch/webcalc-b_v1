import streamlit as st
import math

st.title("🧮 BBCalc:V_1 - Web Version")


category = st.selectbox(
    "Select Category:",
    ["-- Select Category --", "Arithmetic & Basics", "Financial Calculations", "Rectangle", "Square", "Circle", "Triangle", "Unit Conversions"]
)


if category == "Arithmetic & Basics":
    st.subheader("Arithmetic & Basics")
    choice = st.selectbox("Choose Operation", [
        "1. Percentage Calculation", "2. Percentage of a Number", "3. Average", 
        "4. Time", "5. Speed", "6. Distance", "7. Ratio"
    ])
    
    if "1." in choice:
        part = st.number_input("Enter part value", value=0.0)
        total = st.number_input("Enter total value", value=0.0)
        if st.button("Calculate"):
            st.success(f"Percentage: {(part / total) * 100 if total != 0 else 'Error: Division by zero'}%")
            
    elif "2." in choice:
        num = st.number_input("Enter number", value=0.0)
        per = st.number_input("Enter percentage", value=0.0)
        if st.button("Calculate"):
            st.success(f"Result: {(num * per) / 100}")
            
    elif "3." in choice:
        nums_str = st.text_input("Enter numbers separated by space", "0")
        if st.button("Calculate"):
            try:
                nums = list(map(float, nums_str.split()))
                st.success(f"Average: {sum(nums) / len(nums) if nums else 0}")
            except:
                st.error("Please enter valid numbers.")
                
    elif "4." in choice:
        d = st.number_input("Enter distance", value=0.0)
        s = st.number_input("Enter speed", value=0.0)
        if st.button("Calculate"):
            st.success(f"Time: {d / s if s != 0 else 'Error: Speed cannot be zero'}")
            
    elif "5." in choice:
        d = st.number_input("Enter distance", value=0.0)
        t = st.number_input("Enter time", value=0.0)
        if st.button("Calculate"):
            st.success(f"Speed: {d / t if t != 0 else 'Error: Time cannot be zero'}")
            
    elif "6." in choice:
        s = st.number_input("Enter speed", value=0.0)
        t = st.number_input("Enter time", value=0.0)
        if st.button("Calculate"):
            st.success(f"Distance: {s * t}")
            
    elif "7." in choice:
        a = st.number_input("Enter first number (a)", value=0.0)
        b = st.number_input("Enter second number (b)", value=0.0)
        if st.button("Calculate"):
            gcd = math.gcd(int(a), int(b))
            st.success(f"Ratio: {int(a/gcd)} : {int(b/gcd)}" if gcd != 0 else "Ratio: 0 : 0")


elif category == "Financial Calculations":
    st.subheader("Financial Calculations")
    choice = st.selectbox("Choose Operation", [
        "8. Profit", "9. Loss", "10. Profit Percentage", "11. Loss Percentage", 
        "12. Simple Interest", "13. Compound Interest"
    ])
    
    if "8." in choice:
        sp = st.number_input("Enter Selling Price", value=0.0)
        cp = st.number_input("Enter Cost Price", value=0.0)
        if st.button("Calculate"):
            st.success(f"Profit: {sp - cp}")
    elif "9." in choice:
        cp = st.number_input("Enter Cost Price", value=0.0)
        sp = st.number_input("Enter Selling Price", value=0.0)
        if st.button("Calculate"):
            st.success(f"Loss: {cp - sp}")
    elif "10." in choice:
        profit = st.number_input("Enter Profit amount", value=0.0)
        cp = st.number_input("Enter Cost Price", value=0.0)
        if st.button("Calculate"):
            st.success(f"Profit Percentage: {(profit / cp) * 100 if cp != 0 else 0}%")
    elif "11." in choice:
        loss = st.number_input("Enter Loss amount", value=0.0)
        cp = st.number_input("Enter Cost Price", value=0.0)
        if st.button("Calculate"):
            st.success(f"Loss Percentage: {(loss / cp) * 100 if cp != 0 else 0}%")
    elif "12." in choice:
        p = st.number_input("Enter Principal amount", value=0.0)
        r = st.number_input("Enter Annual Interest Rate (%)", value=0.0)
        t = st.number_input("Enter Time (years)", value=0.0)
        if st.button("Calculate"):
            st.success(f"Simple Interest: {(p * r * t) / 100}")
    elif "13." in choice:
        p = st.number_input("Enter Principal amount", value=0.0)
        r = st.number_input("Enter Annual Interest Rate (%)", value=0.0)
        t = st.number_input("Enter Time (years)", value=0.0)
        n = st.number_input("Enter times interest applied per period", value=1.0)
        if st.button("Calculate"):
            st.success(f"Compound Interest: {p * (1 + (r / (100 * n)))**(n * t) - p}")


elif category == "Rectangle":
    st.subheader("Rectangle Calculations")
    choice = st.selectbox("Choose Operation", [
        "14. Area", "15. Perimeter", "16. Diagonal", "17. Aspect Ratio", 
        "18. Circumradius", "19. Center Coordinates", "20. Length from Area & Breadth", 
        "21. Breadth from Area & Length", "22. Length from Perimeter & Breadth", 
        "23. Breadth from Perimeter & Length", "24. Length from Diagonal & Breadth", 
        "25. Breadth from Diagonal & Length"
    ])
    
    if "14." in choice:
        l = st.number_input("Length", value=0.0)
        b = st.number_input("Breadth", value=0.0)
        if st.button("Calculate"): st.success(f"Area: {l * b}")
    elif "15." in choice:
        l = st.number_input("Length", value=0.0)
        b = st.number_input("Breadth", value=0.0)
        if st.button("Calculate"): st.success(f"Perimeter: {2 * (l + b)}")
    elif "16." in choice:
        l = st.number_input("Length", value=0.0)
        b = st.number_input("Breadth", value=0.0)
        if st.button("Calculate"): st.success(f"Diagonal: {math.sqrt(l**2 + b**2)}")
    elif "17." in choice:
        l = st.number_input("Length", value=0.0)
        b = st.number_input("Breadth", value=0.0)
        if st.button("Calculate"):
            gcd = math.gcd(int(l), int(b))
            st.success(f"Aspect Ratio: {int(l/gcd)}:{int(b/gcd)}")
    elif "18." in choice:
        l = st.number_input("Length", value=0.0)
        b = st.number_input("Breadth", value=0.0)
        if st.button("Calculate"): st.success(f"Circumradius: {math.sqrt(l**2 + b**2) / 2}")
    elif "19." in choice:
        x1 = st.number_input("X1", value=0.0)
        y1 = st.number_input("Y1", value=0.0)
        x2 = st.number_input("X2", value=0.0)
        y2 = st.number_input("Y2", value=0.0)
        if st.button("Calculate"): st.success(f"Center Coordinates: {((x1+x2)/2, (y1+y2)/2)}")
    elif "20." in choice:
        area = st.number_input("Area", value=0.0)
        b = st.number_input("Breadth", value=0.0)
        if st.button("Calculate"): st.success(f"Length: {area / b if b != 0 else 0}")
    elif "21." in choice:
        area = st.number_input("Area", value=0.0)
        l = st.number_input("Length", value=0.0)
        if st.button("Calculate"): st.success(f"Breadth: {area / l if l != 0 else 0}")
    elif "22." in choice:
        peri = st.number_input("Perimeter", value=0.0)
        b = st.number_input("Breadth", value=0.0)
        if st.button("Calculate"): st.success(f"Length: {(peri / 2) - b}")
    elif "23." in choice:
        peri = st.number_input("Perimeter", value=0.0)
        l = st.number_input("Length", value=0.0)
        if st.button("Calculate"): st.success(f"Breadth: {(peri / 2) - l}")
    elif "24." in choice:
        diag = st.number_input("Diagonal", value=0.0)
        b = st.number_input("Breadth", value=0.0)
        if st.button("Calculate"): st.success(f"Length: {math.sqrt(max(0, diag**2 - b**2))}")
    elif "25." in choice:
        diag = st.number_input("Diagonal", value=0.0)
        l = st.number_input("Length", value=0.0)
        if st.button("Calculate"): st.success(f"Breadth: {math.sqrt(max(0, diag**2 - l**2))}")


elif category == "Square":
    st.subheader("Square Calculations")
    choice = st.selectbox("Choose Operation", [
        "26. Area", "27. Perimeter", "28. Diagonal", "29. Inradius", 
        "30. Circumradius", "31. Side from Area", "32. Side from Perimeter", "33. Side from Diagonal"
    ])
    
    if "26." in choice:
        s = st.number_input("Side", value=0.0)
        if st.button("Calculate"): st.success(f"Area: {s**2}")
    elif "27." in choice:
        s = st.number_input("Side", value=0.0)
        if st.button("Calculate"): st.success(f"Perimeter: {4 * s}")
    elif "28." in choice:
        s = st.number_input("Side", value=0.0)
        if st.button("Calculate"): st.success(f"Diagonal: {s * math.sqrt(2)}")
    elif "29." in choice:
        s = st.number_input("Side", value=0.0)
        if st.button("Calculate"): st.success(f"Inradius: {s / 2}")
    elif "30." in choice:
        s = st.number_input("Side", value=0.0)
        if st.button("Calculate"): st.success(f"Circumradius: {(s * math.sqrt(2)) / 2}")
    elif "31." in choice:
        area = st.number_input("Area", value=0.0)
        if st.button("Calculate"): st.success(f"Side: {math.sqrt(max(0, area))}")
    elif "32." in choice:
        peri = st.number_input("Perimeter", value=0.0)
        if st.button("Calculate"): st.success(f"Side: {peri / 4}")
    elif "33." in choice:
        diag = st.number_input("Diagonal", value=0.0)
        if st.button("Calculate"): st.success(f"Side: {diag / math.sqrt(2)}")


elif category == "Circle":
    st.subheader("Circle Calculations")
    choice = st.selectbox("Choose Operation", [
        "34. Radius from Diameter", "35. Diameter from Radius", "36. Area", "37. Circumference", 
        "38. Radius from Area", "39. Radius from Circumference", "40. Area of Sector", 
        "41. Perimeter of Sector", "42. Arc Length", "43. Chord Length", 
        "44. Distance to Chord", "45. Area of Segment", "46. Area of Annulus"
    ])
    
    if "34." in choice:
        d = st.number_input("Diameter", value=0.0)
        if st.button("Calculate"): st.success(f"Radius: {d / 2}")
    elif "35." in choice:
        r = st.number_input("Radius", value=0.0)
        if st.button("Calculate"): st.success(f"Diameter: {2 * r}")
    elif "36." in choice:
        r = st.number_input("Radius", value=0.0)
        if st.button("Calculate"): st.success(f"Area: {math.pi * (r**2)}")
    elif "37." in choice:
        r = st.number_input("Radius", value=0.0)
        if st.button("Calculate"): st.success(f"Circumference: {2 * math.pi * r}")
    elif "38." in choice:
        area = st.number_input("Area", value=0.0)
        if st.button("Calculate"): st.success(f"Radius: {math.sqrt(max(0, area / math.pi))}")
    elif "39." in choice:
        circ = st.number_input("Circumference", value=0.0)
        if st.button("Calculate"): st.success(f"Radius: {circ / (2 * math.pi)}")
    elif "40." in choice:
        r = st.number_input("Radius", value=0.0)
        theta = st.number_input("Angle in degrees", value=0.0)
        if st.button("Calculate"): st.success(f"Area of Sector: {(theta / 360) * math.pi * (r**2)}")
    elif "41." in choice:
        r = st.number_input("Radius", value=0.0)
        theta = st.number_input("Angle in degrees", value=0.0)
        if st.button("Calculate"):
            arc = (theta / 360) * 2 * math.pi * r
            st.success(f"Perimeter of Sector: {arc + (2 * r)}")
    elif "42." in choice:
        r = st.number_input("Radius", value=0.0)
        theta = st.number_input("Angle in degrees", value=0.0)
        if st.button("Calculate"): st.success(f"Arc Length: {(theta / 360) * 2 * math.pi * r}")
    elif "43." in choice:
        r = st.number_input("Radius", value=0.0)
        theta = st.number_input("Angle in degrees", value=0.0)
        if st.button("Calculate"): st.success(f"Chord Length: {2 * r * math.sin(math.radians(theta / 2))}")
    elif "44." in choice:
        r = st.number_input("Radius", value=0.0)
        chord = st.number_input("Chord length", value=0.0)
        if st.button("Calculate"): st.success(f"Distance to Chord: {math.sqrt(max(0, r**2 - (chord / 2)**2))}")
    elif "45." in choice:
        r = st.number_input("Radius", value=0.0)
        theta = st.number_input("Angle in degrees", value=0.0)
        if st.button("Calculate"):
            sec_area = (theta / 360) * math.pi * (r**2)
            tri_area = 0.5 * (r**2) * math.sin(math.radians(theta))
            st.success(f"Area of Segment: {sec_area - tri_area}")
    elif "46." in choice:
        R = st.number_input("Outer Radius (R)", value=0.0)
        r = st.number_input("Inner Radius (r)", value=0.0)
        if st.button("Calculate"): st.success(f"Area of Annulus: {math.pi * (R**2 - r**2)}")


elif category == "Triangle":
    st.subheader("Triangle Calculations")
    choice = st.selectbox("Choose Operation", [
        "47. Perimeter", "48. Area (Base & Height)", "49. Area (Heron's Formula)", 
        "50. Area (SAS)", "51. Area (Shoelace Formula)", "52. Hypotenuse", 
        "53. Missing Side (Right Triangle)", "54. Inradius (Right Triangle)", 
        "55. Equilateral Area", "56. Equilateral Perimeter", "57. Equilateral Height", 
        "58. Equilateral Inradius", "59. Equilateral Circumradius", "60. Isosceles Area", 
        "61. Isosceles Perimeter", "62. General Inradius", "63. General Circumradius", 
        "64. Altitude from Area & Base", "65. Median Length", "66. Third Angle"
    ])
    
    if "47." in choice:
        a = st.number_input("Side a", value=0.0)
        b = st.number_input("Side b", value=0.0)
        c = st.number_input("Side c", value=0.0)
        if st.button("Calculate"): st.success(f"Perimeter: {a + b + c}")
    elif "48." in choice:
        base = st.number_input("Base", value=0.0)
        height = st.number_input("Height", value=0.0)
        if st.button("Calculate"): st.success(f"Area: {0.5 * base * height}")
    elif "49." in choice:
        a = st.number_input("Side a", value=0.0)
        b = st.number_input("Side b", value=0.0)
        c = st.number_input("Side c", value=0.0)
        if st.button("Calculate"):
            s = (a + b + c) / 2
            val = s * (s - a) * (s - b) * (s - c)
            st.success(f"Area (Heron's): {math.sqrt(max(0, val))}")
    elif "50." in choice:
        a = st.number_input("Side a", value=0.0)
        b = st.number_input("Side b", value=0.0)
        angle_c = st.number_input("Included Angle C (degrees)", value=0.0)
        if st.button("Calculate"): st.success(f"Area (SAS): {0.5 * a * b * math.sin(math.radians(angle_c))}")
    elif "51." in choice:
        x1 = st.number_input("X1", value=0.0)
        y1 = st.number_input("Y1", value=0.0)
        x2 = st.number_input("X2", value=0.0)
        y2 = st.number_input("Y2", value=0.0)
        x3 = st.number_input("X3", value=0.0)
        y3 = st.number_input("Y3", value=0.0)
        if st.button("Calculate"): st.success(f"Area (Shoelace): {0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))}")
    elif "52." in choice:
        p = st.number_input("Perpendicular", value=0.0)
        b = st.number_input("Base", value=0.0)
        if st.button("Calculate"): st.success(f"Hypotenuse: {math.sqrt(p**2 + b**2)}")
    elif "53." in choice:
        hyp = st.number_input("Hypotenuse", value=0.0)
        other = st.number_input("Other side", value=0.0)
        if st.button("Calculate"): st.success(f"Missing side: {math.sqrt(max(0, hyp**2 - other**2))}")
    elif "54." in choice:
        p = st.number_input("Perpendicular", value=0.0)
        b = st.number_input("Base", value=0.0)
        if st.button("Calculate"):
            hyp = math.sqrt(p**2 + b**2)
            st.success(f"Inradius: {(p + b - hyp) / 2}")
    elif "55." in choice:
        a = st.number_input("Side", value=0.0)
        if st.button("Calculate"): st.success(f"Area: {(math.sqrt(3) / 4) * (a**2)}")
    elif "56." in choice:
        a = st.number_input("Side", value=0.0)
        if st.button("Calculate"): st.success(f"Perimeter: {3 * a}")
    elif "57." in choice:
        a = st.number_input("Side", value=0.0)
        if st.button("Calculate"): st.success(f"Height: {(math.sqrt(3) / 2) * a}")
    elif "58." in choice:
        a = st.number_input("Side", value=0.0)
        if st.button("Calculate"): st.success(f"Inradius: {a / (2 * math.sqrt(3))}")
    elif "59." in choice:
        a = st.number_input("Side", value=0.0)
        if st.button("Calculate"): st.success(f"Circumradius: {a / math.sqrt(3)}")
    elif "60." in choice:
        a = st.number_input("Equal side (a)", value=0.0)
        b = st.number_input("Base (b)", value=0.0)
        if st.button("Calculate"):
            height = math.sqrt(max(0, a**2 - (b**2 / 4)))
            st.success(f"Area: {0.5 * b * height}")
    elif "61." in choice:
        a = st.number_input("Equal side (a)", value=0.0)
        b = st.number_input("Base (b)", value=0.0)
        if st.button("Calculate"): st.success(f"Perimeter: {(2 * a) + b}")
    elif "62." in choice:
        area = st.number_input("Area", value=0.0)
        s = st.number_input("Semi-perimeter", value=0.0)
        if st.button("Calculate"): st.success(f"Inradius: {area / s if s != 0 else 0}")
    elif "63." in choice:
        a = st.number_input("Side a", value=0.0)
        b = st.number_input("Side b", value=0.0)
        c = st.number_input("Side c", value=0.0)
        area = st.number_input("Area", value=0.0)
        if st.button("Calculate"): st.success(f"Circumradius: {(a * b * c) / (4 * area) if area != 0 else 0}")
    elif "64." in choice:
        area = st.number_input("Area", value=0.0)
        base = st.number_input("Base", value=0.0)
        if st.button("Calculate"): st.success(f"Altitude: {(2 * area) / base if base != 0 else 0}")
    elif "65." in choice:
        a = st.number_input("Side a", value=0.0)
        b = st.number_input("Side b", value=0.0)
        c = st.number_input("Side c", value=0.0)
        if st.button("Calculate"): st.success(f"Median: {0.5 * math.sqrt(max(0, 2 * b**2 + 2 * c**2 - a**2))}")
    elif "66." in choice:
        angle1 = st.number_input("First angle", value=0.0)
        angle2 = st.number_input("Second angle", value=0.0)
        if st.button("Calculate"): st.success(f"Third Angle: {180 - (angle1 + angle2)}")


elif category == "Unit Conversions":
    st.subheader("Unit Conversions")
    choice = st.selectbox("Choose Operation", [
        "67. Centimetres to Metres", "68. Metres to Kilometres", "69. Grams to Kilograms", 
        "70. Kilograms to Grams", "71. Celsius to Fahrenheit", "72. Fahrenheit to Celsius"
    ])
    
    if "67." in choice:
        cm = st.number_input("Centimetres", value=0.0)
        if st.button("Calculate"): st.success(f"Metres: {cm / 100}")
    elif "68." in choice:
        m = st.number_input("Metres", value=0.0)
        if st.button("Calculate"): st.success(f"Kilometres: {m / 1000}")
    elif "69." in choice:
        g = st.number_input("Grams", value=0.0)
        if st.button("Calculate"): st.success(f"Kilograms: {g / 1000}")
    elif "70." in choice:
        kg = st.number_input("Kilograms", value=0.0)
        if st.button("Calculate"): st.success(f"Grams: {kg * 1000}")
    elif "71." in choice:
        c = st.number_input("Celsius", value=0.0)
        if st.button("Calculate"): st.success(f"Fahrenheit: {(c * 9/5) + 32}")
    elif "72." in choice:
        f = st.number_input("Fahrenheit", value=0.0)
        if st.button("Calculate"): st.success(f"Celsius: {(f - 32) * 5/9}")
