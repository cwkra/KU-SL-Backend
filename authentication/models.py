from django.contrib.auth.models import AbstractUser
from django.db import models

FACULTY_CHOICES = [
    ('Agriculture', 'เกษตร'),
    ('Business Administration', 'บริหารธุรกิจ'),
    ('Fisheries', 'ประมง'),
    ('Humanities', 'มนุษยศาสตร์'),
    ('Forestry', 'วนศาสตร์'),
    ('Science', 'วิทยาศาสตร์'),
    ('Engineering', 'วิศวกรรมศาสตร์'),
    ('Education', 'ศึกษาศาสตร์'),
    ('Economics', 'เศรษฐศาสตร์'),
    ('Architecture', 'สถาปัตยกรรมศาสตร์'),
    ('Social Sciences', 'สังคมศาสตร์'),
    ('Veterinary Medicine', 'สัตวแพทยศาสตร์'),
    ('Argo-Industry', 'อุตสาหกรรมเกษตร'),
    ('Veterinary Technology', 'เทคนิคการสัตวแพทย์'),
    ('Environment', 'สิ่งแวดล้อม'),
    ('Medicine', 'แพทยศาสตร์'),
    ('Nursing', 'พยาบาลศาสตร์'),
    ('Interdisciplinary Management and Technology', 'สหวิทยาการจัดการและเทคโนโลยี'),
    ('Integrated Science', 'วิทยาลัยบูรณาการศาสตร์'),
    ('The Graduate School', 'บัณฑิตวิทยาลัย'),
    ('International Studies Establishment Project', 'โครงการจัดตั้งวิทยาลัยนานาชาติ')
]

DEPARTMENT_CHOICES = [
    # เกษตร
    ('Entomology', 'กีฏวิทยา'),
    ('Farm Mechanics', 'เกษตรกลวิธาน'),
    ('Home Economics', 'คหกรรมศาสตร์'),
    ('Soil Science', 'ปฐพีวิทยา'),
    ('Agronomy', 'พืชไร่นา'),
    ('Horticulture', 'พืชสวน'),
    ('Plant Pathology', 'โรคพืช'),
    ('Agricultural Extension and Communication', 'ส่งเสริมและนิเทศศาสตร์เกษตร'),
    ('Animal Science', 'สัตวบาล'),
    # บริหาร
    ('Finance', 'การเงิน'),
    ('Management', 'การจัดการ'),
    ('Operations Management', 'การจัดการเทคโนโลยีและการปฏิบัติการ'),
    ('Marketing', 'การตลาด'),
    ('Accounting', 'บัญชี'),
    # ประมง
    ('Fishery Management', 'การจัดการประมง'),
    ('Fishery Biology', 'ชีววิทยาประมง'),
    ('Fishery Products', 'ผลิตภัณฑ์ประมง'),
    ('Aquaculture', 'เพาะเลี้ยงสัตว์น้ำ'),
    ('Marine Science', 'วิทยาศาสตร์ทางทะเล'),
    # มนุษยศาสตร์
    ('Music', 'ดนตรี'),
    ('Communication Arts and Information Science', 'นิเทศศาสตร์และสารสนเทศศาสตร์'),
    ('Foreign Languages', 'ภาษาต่างประเทศ'),
    ('Literature', 'วรรณคดี'),
    ('Linguistics', 'ภาษาศาสตร์'),
    ('Thai Language', 'ภาษาไทย'),
    ('Eastern Languages', 'ภาษาตะวันออก'),
    ('Philosophy and Religion', 'ปรัชญาและศาสนา'),
    ('Tourism and Hospitality Industry', 'อุตสาหกรรมท่องเที่ยวและบริการ'),
    # วนศาสตร์
    ('Forest Management', 'การจัดการป่าไม้'),
    ('Forest Biology', 'ชีววิทยาป่าไม้'),
    ('Forest Engineering', 'วิศวกรรมป่าไม้'),
    ('Forest Products', 'วนผลิตภัณฑ์'),
    ('Silviculture', 'วนวัฒนวิทยา'),
    ('Conservation', 'อนุรักษวิทยา'),
    # วิทยาศาสตร์
    ('Mathematics', 'คณิตศาสตร์'),
    ('Chemistry', 'เคมี'),
    ('Microbiology', 'จุลชีววิทยา'),
    ('Biochemistry', 'ชีวเคมี'),
    ('Botany', 'พฤกษศาสตร์'),
    ('Genetics', 'พันธุศาสตร์'),
    ('Physics', 'ฟิสิกส์'),
    ('Applied Radiation and Isotope', 'รังสีประยุกต์และไอโซโทป'),
    ('Computer Science', 'วิทยาการคอมพิวเตอร์'),
    ('Earth Science', 'วิทยาศาสตร์พื้นพิภพ'),
    ('Materials Science', 'วัสดุศาสตร์'),
    ('Statistics', 'สถิติ'),
    ('Zoology', 'สัตววิทยา'),
    # วิศวกรรมศาสตร์
    ('Aerospace Engineering', 'วิศวกรรมการบินและอวกาศ'),
    ('Computer Engineering', 'วิศวกรรมคอมพิวเตอร์'),
    ('Chemical Engineering', 'วิศวกรรมเคมี'),
    ('Mechanical Engineering', 'วิศวกรรมเครื่องกล'),
    ('Water Resources Engineering', 'วิศวกรรมทรัพยากรน้ำ'),
    ('Electrical Engineering', 'วิศวกรรมไฟฟ้า'),
    ('Materials Engineering', 'วิศวกรรมวัสดุ'),
    ('Civil Engineering', 'วิศวกรรมโยธา'),
    ('Environmental Engineering', 'วิศวกรรมสิ่งแวดล้อม'),
    ('Industrial Engineering', 'วิศวกรรมอุตสาหการ'),
    # ศึกษาศาสตร์
    ('Education', ''),
    ('Educational Psychology and Guidance', ''),
    ('Educational Technology', ''),
    ('Physical Education', ''),
    ('Vocational Education', ''),
    # เศรษฐศาสตร์
    ('Economics', 'เศรษฐศาสตร์'),
    ('Agricultural and Resource Economics', 'เศรษฐศาสตร์เกษตรและทรัพยากร'),
    ('Cooperative', 'สหกรณ์'),
    # สถาปัตยกรรม
    ('Architecture', 'สถาปัตยกรรม'),
    ('Landscape Architecture', 'ภูมิสถาปัตยกรรม'),
    ('Building Innovation and Technology', 'นวัตกรรมอาคาร'),
    # สังคมศาสตร์
    ('Psychology', 'จิตวิทยา'),
    ('Law', 'นิติศาสตร์'),
    ('History', 'ประวัติศาสตร์'),
    ('Geography', 'ภูมิศาสตร์'),
    ('Political Science and Public Administration', 'รัฐศาสตร์และรัฐประศาสนศาษตร์'),
    ('Sociology and Anthropology', 'สังคมวิทยาและมานุษยวิทยา'),
    ('Graduate Interdisciplinary Program in Social Development', 'โครงการสหวิทยาการระดับบัณฑิตศึกษา สาขาพัฒนาสังคม'),
    ('Special Program in Southeast Asian Studies', 'โครงการเอเชียตะวันออกเฉียงใต้ภาคพิเศษ'),
    # สัตวแพทยศาสตร์
    ('Anatomy', 'กายวิภาคศาสตร์'),
    ('Physiology', 'สรีรวิทยา'),
    ('Microbiology and Immunology', 'จุลชีววิทยาและวิทยาภูมิคุ้มกัน'),
    ('Pharmacology', 'เภสัชวิทยา'),
    ('Pathology', 'พยาธิวิทยา'),
    ('Parasitology', 'ปรสิตวิทยา'),
    # อุตสาหกรรมเกษตร
    ('Agro-Industrial Technology', 'เทคโนโลยีอุตสาหกรรมเกษตร'),
    ('Biotechnology', 'เทคโนโลยีชีวภาพ'),
    ('Food Science & Technology', 'วิทยาศาสตร์และเทคโนโลยีการอาหาร'),
    ('Packaging & Materials Technology', 'เทคโนโลยีการบรรจุ และวัสดุ'),
    ('Product Development', 'พัฒนาผลิตภัณฑ์'),
    ('Textile Science', 'วิทยาการสิ่งทอ'),
    ('Agro-Industrial Innovation and Technology (International Program) (AIIP)', 'นวัตกรรมและเทคโนโลยีอุตสาหกรรมเกษตร (หลักสูตรนานาชาติ)'),
    # เทคนิคการสัตวแพทย์
    ('Veterinary Technology', 'เทคนิคการสัตวแพทย์'),
    ('Animal Nursing (Special Program)', 'สาขาวิชาการพยาบาลสัตว์ (ภาคพิเศษ)'),
    ('Veterinary Technology (Special Program)', 'สาขาวิชาเทคนิคการสัตวแพทย์ (ภาคพิเศษ)'),
    # สิ่งแวดล้อม
    ('Environmental Technology and Management', 'เทคโนโลยีและการจัดการสิ่งแวดล้อม'),
    ('Environmental Science', 'วิทยาศาสตร์สิ่งแวดล้อม'),
    # แพทยศาสตร์
    ('Medicine', 'แพทยศาสตร์'),
    # พยาบาลศาสตร์
    ('Nursing Science', 'พยาบาลศาสตร์'),
    # สหวิทยาการจัดการและเทคโนโลยี
    ('Cultural and Health Tourism Management', 'การจัดการท่องเที่ยวเชิงวัฒนธรรมและสุขภาพ'),
    ('Hospitality Industry Management', 'การจัดการอุตสาหกรรมการบริการ'),
]

EDUCATION_LEVEL_CHOICES = [
    ('BACHELOR_DEGREE', 'ปริญญาตรี'),
    ('MASTER_DEGREE', 'ปริญญาโท'),
    ('DOCTOR_DEGREE', 'ปริญญาเอก')
]

STATUS_CHOICES = [
    ('NEW_BORROWER', 'ผู้กู้ยืมรายใหม่'),
    ('OLD_BORROWER', 'ผู้กู้ยืมรายเก่า')
]

# Create your models here.
class Education(models.Model):
    student_id_number = models.CharField(max_length=10, unique=True)
    faculty = models.CharField(max_length=150, choices=FACULTY_CHOICES)
    department = models.CharField(max_length=150, choices=DEPARTMENT_CHOICES)
    education_level = models.CharField(max_length=150, choices=EDUCATION_LEVEL_CHOICES)
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default='NEW_BORROWER')
    
    
class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    tel_number = models.CharField(max_length=20, unique=True)
    identity_card_number = models.CharField(max_length=13, unique=True)
    image = models.ImageField(upload_to='private/profile/')
    education = models.OneToOneField(Education, null=True, on_delete=models.CASCADE, blank=True)
    last_login = None
    first_name = None
    last_name = None
    date_joined = None

