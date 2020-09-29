def kg2g(so_can_kg):
    # Tra ra so can sau khi da doi sang gam
    gam = so_can_kg * 1000
    return gam

def m2mm(so_met):
    # Tra ra so mm
    mm = so_met * 1000
    return mm

chon = -1
while chon!=0:
    print("0-Thoat,1-Kg 2 gam,2-Met 2 mm");
    chon  =int (input("Nhap lua chon"))
    if chon==1:
        # doi tu kg sang gam
        kg = int(input("Nhap vao so kg"))
        g = kg2g(kg)
        print("So gam  = ", g)
    elif chon==2:
        # doi tu met sang mm
        m = int(input("Nhap vao so met"))
        mm = m2mm(m)
        print("So mm  = ", mm)
    else:
        print("Tam biet ban!")