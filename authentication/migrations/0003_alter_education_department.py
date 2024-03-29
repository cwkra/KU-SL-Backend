# Generated by Django 4.2.7 on 2024-02-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='department',
            field=models.CharField(choices=[('Entomology', 'กีฏวิทยา'), ('Farm Mechanics', 'เกษตรกลวิธาน'), ('Home Economics', 'คหกรรมศาสตร์'), ('Soil Science', 'ปฐพีวิทยา'), ('Agronomy', 'พืชไร่นา'), ('Horticulture', 'พืชสวน'), ('Plant Pathology', 'โรคพืช'), ('Agricultural Extension and Communication', 'ส่งเสริมและนิเทศศาสตร์เกษตร'), ('Animal Science', 'สัตวบาล'), ('Finance', 'การเงิน'), ('Management', 'การจัดการ'), ('Operations Management', 'การจัดการเทคโนโลยีและการปฏิบัติการ'), ('Marketing', 'การตลาด'), ('Accounting', 'บัญชี'), ('Fishery Management', 'การจัดการประมง'), ('Fishery Biology', 'ชีววิทยาประมง'), ('Fishery Products', 'ผลิตภัณฑ์ประมง'), ('Aquaculture', 'เพาะเลี้ยงสัตว์น้ำ'), ('Marine Science', 'วิทยาศาสตร์ทางทะเล'), ('Music', 'ดนตรี'), ('Communication Arts and Information Science', 'นิเทศศาสตร์และสารสนเทศศาสตร์'), ('Foreign Languages', 'ภาษาต่างประเทศ'), ('Literature', 'วรรณคดี'), ('Linguistics', 'ภาษาศาสตร์'), ('Thai Language', 'ภาษาไทย'), ('Eastern Languages', 'ภาษาตะวันออก'), ('Philosophy and Religion', 'ปรัชญาและศาสนา'), ('Tourism and Hospitality Industry', 'อุตสาหกรรมท่องเที่ยวและบริการ'), ('Forest Management', 'การจัดการป่าไม้'), ('Forest Biology', 'ชีววิทยาป่าไม้'), ('Forest Engineering', 'วิศวกรรมป่าไม้'), ('Forest Products', 'วนผลิตภัณฑ์'), ('Silviculture', 'วนวัฒนวิทยา'), ('Conservation', 'อนุรักษวิทยา'), ('Mathematics', 'คณิตศาสตร์'), ('Chemistry', 'เคมี'), ('Microbiology', 'จุลชีววิทยา'), ('Biochemistry', 'ชีวเคมี'), ('Botany', 'พฤกษศาสตร์'), ('Genetics', 'พันธุศาสตร์'), ('Physics', 'ฟิสิกส์'), ('Applied Radiation and Isotope', 'รังสีประยุกต์และไอโซโทป'), ('Computer Science', 'วิทยาการคอมพิวเตอร์'), ('Earth Science', 'วิทยาศาสตร์พื้นพิภพ'), ('Materials Science', 'วัสดุศาสตร์'), ('Statistics', 'สถิติ'), ('Zoology', 'สัตววิทยา'), ('Aerospace Engineering', 'วิศวกรรมการบินและอวกาศ'), ('Computer Engineering', 'วิศวกรรมคอมพิวเตอร์'), ('Chemical Engineering', 'วิศวกรรมเคมี'), ('Mechanical Engineering', 'วิศวกรรมเครื่องกล'), ('Water Resources Engineering', 'วิศวกรรมทรัพยากรน้ำ'), ('Electrical Engineering', 'วิศวกรรมไฟฟ้า'), ('Materials Engineering', 'วิศวกรรมวัสดุ'), ('Civil Engineering', 'วิศวกรรมโยธา'), ('Environmental Engineering', 'วิศวกรรมสิ่งแวดล้อม'), ('Industrial Engineering', 'วิศวกรรมอุตสาหการ'), ('Education', 'การศึกษา'), ('Educational Psychology and Guidance', 'จิตวิทยาการศึกษาและการแนะแนว'), ('Educational Technology', 'เทคโนโลยีการศึกษา'), ('Physical Education', 'พลศึกษา'), ('Vocational Education', 'อาชีวศึกษา'), ('Economics', 'เศรษฐศาสตร์'), ('Agricultural and Resource Economics', 'เศรษฐศาสตร์เกษตรและทรัพยากร'), ('Cooperative', 'สหกรณ์'), ('Architecture', 'สถาปัตยกรรม'), ('Landscape Architecture', 'ภูมิสถาปัตยกรรม'), ('Building Innovation and Technology', 'นวัตกรรมอาคาร'), ('Psychology', 'จิตวิทยา'), ('Law', 'นิติศาสตร์'), ('History', 'ประวัติศาสตร์'), ('Geography', 'ภูมิศาสตร์'), ('Political Science and Public Administration', 'รัฐศาสตร์และรัฐประศาสนศาษตร์'), ('Sociology and Anthropology', 'สังคมวิทยาและมานุษยวิทยา'), ('Graduate Interdisciplinary Program in Social Development', 'โครงการสหวิทยาการระดับบัณฑิตศึกษา สาขาพัฒนาสังคม'), ('Special Program in Southeast Asian Studies', 'โครงการเอเชียตะวันออกเฉียงใต้ภาคพิเศษ'), ('Anatomy', 'กายวิภาคศาสตร์'), ('Physiology', 'สรีรวิทยา'), ('Microbiology and Immunology', 'จุลชีววิทยาและวิทยาภูมิคุ้มกัน'), ('Pharmacology', 'เภสัชวิทยา'), ('Pathology', 'พยาธิวิทยา'), ('Parasitology', 'ปรสิตวิทยา'), ('Agro-Industrial Technology', 'เทคโนโลยีอุตสาหกรรมเกษตร'), ('Biotechnology', 'เทคโนโลยีชีวภาพ'), ('Food Science & Technology', 'วิทยาศาสตร์และเทคโนโลยีการอาหาร'), ('Packaging & Materials Technology', 'เทคโนโลยีการบรรจุ และวัสดุ'), ('Product Development', 'พัฒนาผลิตภัณฑ์'), ('Textile Science', 'วิทยาการสิ่งทอ'), ('Agro-Industrial Innovation and Technology (International Program) (AIIP)', 'นวัตกรรมและเทคโนโลยีอุตสาหกรรมเกษตร (หลักสูตรนานาชาติ)'), ('Veterinary Technology', 'เทคนิคการสัตวแพทย์'), ('Animal Nursing (Special Program)', 'สาขาวิชาการพยาบาลสัตว์ (ภาคพิเศษ)'), ('Veterinary Technology (Special Program)', 'สาขาวิชาเทคนิคการสัตวแพทย์ (ภาคพิเศษ)'), ('Environmental Technology and Management', 'เทคโนโลยีและการจัดการสิ่งแวดล้อม'), ('Environmental Science', 'วิทยาศาสตร์สิ่งแวดล้อม'), ('Medicine', 'แพทยศาสตร์'), ('Nursing Science', 'พยาบาลศาสตร์'), ('Cultural and Health Tourism Management', 'การจัดการท่องเที่ยวเชิงวัฒนธรรมและสุขภาพ'), ('Hospitality Industry Management', 'การจัดการอุตสาหกรรมการบริการ')], max_length=150),
        ),
    ]