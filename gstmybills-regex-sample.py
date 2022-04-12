# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import re

scanlist = [	"MARGN FREE MARKET ELAMKULAM KALLAMPALLY SREEKARYAM Phone 8075022459 GST RU1E 2017 TAX INVOICE   CASH GST32AYJPA2616F1Z2 DATE 1003 2022  08 48 21 C  2 Bill No80412 CCP ltem Name MRP Qty Rate Total   LAYS20 20 00 1 000 19 39 19 39   CADBURY OREO DO 40 00 2 000 38 54 77 08 S CADBURY GEMS BA 45 00 1 000 43 80 43 80  TIMS GINGELLYB  GoODLY BANANA C   AMUL CHOCO CARA 40 00 1 000 38 08 38 08 70 00 1 000 66 27 66 27 200 00 1 000 194 70 194 70  GOODLY MIXTURE 55 00 1 000 52 06 52 06   G0ODLY FRYUMSS1 45 00 1 000 42 59 42 59   BOUNTY 57G 55 00 1 000 53 55 53 55 S SNICKERS 20  20 00 2 000 19 47 38 94 Round Off   0 46 Total 626 00 Total Itenms 10",
		"TaxPayers ome TaxPayers GSTIN Taxpayer Trad 32DQQPM1743D1ZY NATIONAL MEDI 32BIJPD8548N2ZT Rajan D 32BEAP3990 K2ZF NEDUMANGAD F 32BDOPN1952L1Z8 KERALA STATE SE STAFF FEDERATIO 32ACMPP5981 F2ZA KOCHI KITCHENE 32AAFAG7821H1ZV GASTON FOUNDA CHARITABLE SOC Showing 1 to 6 of 6 entries  filtered from 10 O",
		"Choice1531 S1mis Complex  Hotel Pooram lntemational Buildg  1TRON1C Choice Pesidenl Baza  Kurupa Rad  Thissur  60 01 Bill of Supply Ph 0487 2427629 2427567 E mail tronicchoice yahoo co iniSTIN  32AABFT3086C1ZL COMPUTER  ELECTRONICS  BOOKS  PERIPHERALS  ACCESSORIES  SPARES 4660 Serial Number Date of Issue 09072020cOMPOSIT DEALER State  Kerala State Code  3 Details of Receiver Billed to Details of Consignee Shipped to Name Address Mr  ANIL THIR00R Name   Address Ph 440 10IU Ph State Code   State GSTINUIN  HSN ACS State Code  UOM Qty Less Value of Description of Product Service Rate Amount Dis  Supply 1 990 790 90 1 FiwGERS WIRGLsS 07 HGAD SE 12214 SNo HY 90O43591 1220 Total Terms and Conditions For PONIC FCholce Common Seal Autkofised Signatory true and correct",
		"Reg  Office  P B No  1  Anayara P O   Trivandrum  695 T  91 471 2941000  29414O0 E   feedback tvm kimshealths www kimshealth org CIN  U85110KL1995PLCOOS GSTIN  32AABCT2300C1ZCI State   Kerala State Code  A PROJECT OF KIMS HEALTH CARE MANAGE KIMSHEALTH BILL OF SUPPLY  Original for the Recepient    OP Credit Patient Name  Amal K J   Ibs Invoice No  CO06829822 MRNo  002110909 Invoice Date  11 Feb 2022 02 27 PM Dept  Respiratory Medicine Doctor  Vinod Kumar Kesavan Scheme  Ibs Room No  2503 SI No  Name of Product Service Gross Discount A HSNSAC 1 FIRST 450 00 0 00 Token No  10A Appointment Time  11 Feb 2022 14 15 PM Total Amount  450 00 0 00 REMARKS",
		"Tax Invoice Dated Mas Traders Tc 92 3073 1  Anayara Opp South Park Maruthi Showroom Tnvandrum GSTIN UIN 32ABDFM5661M1Z2 State Name  Kerala  Code 32 Contact  9447935510 9074679299 E Mail  mastraderstvm gmail com Invoice No M SA6818 Delivery Note 6 Nov 2021 Mode Tems of Payment Other Reference S  Supplier s Ref Dated Buyer Buyers Order No AMAL Delivery Note Date Despatch Document No State Name Kerala  Code 32 Destination Despatched through Tems of Delivery Contact Description of Goods HSN SAC GST Quantity Rate per Amount N Rate PC Diamond Blue 7ft 2mm  Lazerlite  3920619018  84 000 Sqft 80 51 Sqgft 6 762 608 Output CGST 9  Output SGS T 9  Round Of 608 Less Total 84 000 Sqft 7 98 Amount Chargeable  in words  INR Seven Thousand Nine Hundred Eighty Only Taxable Value Central Tax Amount 608 66 608 66 State Tax Rate Amount 6 762 84 6 762 84 Rate 9  Tax 608 66 608 66 9  Total  Tax Amount  in words  INR One Thousand Two Hundred Seventeen and Thirty Two paise Only Companys Bank Details Bank Name STATE BANK OF INDIA 38361906807 Branch   FS Code  PALLIPPURAM  SBINO07 Alc No  for Ma Declaration We declare that this invoice shows the actual price of the goods described and that all particulars are true and correct Prepared by Verified by SUBJECT TO TRIVANDRUM JURISDICTION This is a Computer Generated Invoice LO",
		"AquaGrand PROVISION INVOICE Date  l22     Experts In Water Purifier Service CUM CASH RECEIPT 39973 Bill No  2021                  Name  1st Floor  KP6 825  Lavanya Shopping Complex  Near Santhivila Public Market  Nemam  Thiruvananthapuram   6950220 GST No  32DTPPP0505L 1 ZJ  098078 83333 Address  hRnkMttukonaM Ti Model 4ub Flo Dx U Bhym  D  hone No  4HE Dla GST No  SL No Make  q Technician Name  Amount Description Quantity Rate Total  A  Technician Remarks JpAA AL  Labour Charges  B  TOTAL  A B  hoal     ases                       hoinge ol                               s  2022 03 04 12 24 Anu reneat complaint arising out within 7 days from bill date has to be u foult renorted after Received with thanks  the sum of"]


# without statecode check
#regex_gst = "\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}" 

# with statecode check
#regex_gst = "([0][1-9]|[1-2][0-9]|[3][0-7])[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}" 

# Kerala GSTINs only
regex_gst = "(32)[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}(Z)[A-Z\d]{1}" 

p = re.compile(regex_gst)

try:
  
  for scan in scanlist:

    scan = scan.replace(" ", "")
    scan = scan.replace("\t", "")
    print("\n" + scan)
    m = p.search(scan)
    print("\n ********* " + m.group(0) + " *********")
  #for scan in scanlist:
    #print("scan_text" + str(i) + ": " + p.search(scan).group(0))

except AttributeError:
    print("can't make a group")

