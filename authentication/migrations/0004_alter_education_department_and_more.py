# Generated by Django 4.2.7 on 2024-02-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_education_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='department',
            field=models.CharField(choices=[('กีฏวิทยา', 'กีฏวิทยา'), ('เกษตรกลวิธาน', 'เกษตรกลวิธาน'), ('คหกรรมศาสตร์', 'คหกรรมศาสตร์'), ('ปฐพีวิทยา', 'ปฐพีวิทยา'), ('พืชไร่นา', 'พืชไร่นา'), ('พืชสวน', 'พืชสวน'), ('โรคพืช', 'โรคพืช'), ('ส่งเสริมและนิเทศศาสตร์เกษตร', 'ส่งเสริมและนิเทศศาสตร์เกษตร'), ('สัตวบาล', 'สัตวบาล'), ('การเงิน', 'การเงิน'), ('การจัดการ', 'การจัดการ'), ('การจัดการเทคโนโลยีและการปฏิบัติการ', 'การจัดการเทคโนโลยีและการปฏิบัติการ'), ('การตลาด', 'การตลาด'), ('บัญชี', 'บัญชี'), ('การจัดการประมง', 'การจัดการประมง'), ('ชีววิทยาประมง', 'ชีววิทยาประมง'), ('ผลิตภัณฑ์ประมง', 'ผลิตภัณฑ์ประมง'), ('เพาะเลี้ยงสัตว์น้ำ', 'เพาะเลี้ยงสัตว์น้ำ'), ('วิทยาศาสตร์ทางทะเล', 'วิทยาศาสตร์ทางทะเล'), ('ดนตรี', 'ดนตรี'), ('นิเทศศาสตร์และสารสนเทศศาสตร์', 'นิเทศศาสตร์และสารสนเทศศาสตร์'), ('ภาษาต่างประเทศ', 'ภาษาต่างประเทศ'), ('วรรณคดี', 'วรรณคดี'), ('ภาษาศาสตร์', 'ภาษาศาสตร์'), ('ภาษาไทย', 'ภาษาไทย'), ('ภาษาตะวันออก', 'ภาษาตะวันออก'), ('ปรัชญาและศาสนา', 'ปรัชญาและศาสนา'), ('อุตสาหกรรมท่องเที่ยวและบริการ', 'อุตสาหกรรมท่องเที่ยวและบริการ'), ('การจัดการป่าไม้', 'การจัดการป่าไม้'), ('ชีววิทยาป่าไม้', 'ชีววิทยาป่าไม้'), ('วิศวกรรมป่าไม้', 'วิศวกรรมป่าไม้'), ('วนผลิตภัณฑ์', 'วนผลิตภัณฑ์'), ('วนวัฒนวิทยา', 'วนวัฒนวิทยา'), ('อนุรักษวิทยา', 'อนุรักษวิทยา'), ('คณิตศาสตร์', 'คณิตศาสตร์'), ('เคมี', 'เคมี'), ('จุลชีววิทยา', 'จุลชีววิทยา'), ('ชีวเคมี', 'ชีวเคมี'), ('พฤกษศาสตร์', 'พฤกษศาสตร์'), ('พันธุศาสตร์', 'พันธุศาสตร์'), ('ฟิสิกส์', 'ฟิสิกส์'), ('รังสีประยุกต์และไอโซโทป', 'รังสีประยุกต์และไอโซโทป'), ('วิทยาการคอมพิวเตอร์', 'วิทยาการคอมพิวเตอร์'), ('วิทยาศาสตร์พื้นพิภพ', 'วิทยาศาสตร์พื้นพิภพ'), ('วัสดุศาสตร์', 'วัสดุศาสตร์'), ('สถิติ', 'สถิติ'), ('สัตววิทยา', 'สัตววิทยา'), ('วิศวกรรมการบินและอวกาศ', 'วิศวกรรมการบินและอวกาศ'), ('วิศวกรรมคอมพิวเตอร์', 'วิศวกรรมคอมพิวเตอร์'), ('วิศวกรรมเคมี', 'วิศวกรรมเคมี'), ('วิศวกรรมเครื่องกล', 'วิศวกรรมเครื่องกล'), ('วิศวกรรมทรัพยากรน้ำ', 'วิศวกรรมทรัพยากรน้ำ'), ('วิศวกรรมไฟฟ้า', 'วิศวกรรมไฟฟ้า'), ('วิศวกรรมวัสดุ', 'วิศวกรรมวัสดุ'), ('วิศวกรรมโยธา', 'วิศวกรรมโยธา'), ('วิศวกรรมสิ่งแวดล้อม', 'วิศวกรรมสิ่งแวดล้อม'), ('วิศวกรรมอุตสาหการ', 'วิศวกรรมอุตสาหการ'), ('การศึกษา', 'การศึกษา'), ('จิตวิทยาการศึกษาและการแนะแนว', 'จิตวิทยาการศึกษาและการแนะแนว'), ('เทคโนโลยีการศึกษา', 'เทคโนโลยีการศึกษา'), ('พลศึกษา', 'พลศึกษา'), ('อาชีวศึกษา', 'อาชีวศึกษา'), ('เศรษฐศาสตร์', 'เศรษฐศาสตร์'), ('เศรษฐศาสตร์เกษตรและทรัพยากร', 'เศรษฐศาสตร์เกษตรและทรัพยากร'), ('สหกรณ์', 'สหกรณ์'), ('สถาปัตยกรรม', 'สถาปัตยกรรม'), ('ภูมิสถาปัตยกรรม', 'ภูมิสถาปัตยกรรม'), ('นวัตกรรมอาคาร', 'นวัตกรรมอาคาร'), ('จิตวิทยา', 'จิตวิทยา'), ('นิติศาสตร์', 'นิติศาสตร์'), ('ประวัติศาสตร์', 'ประวัติศาสตร์'), ('ภูมิศาสตร์', 'ภูมิศาสตร์'), ('รัฐศาสตร์และรัฐประศาสนศาษตร์', 'รัฐศาสตร์และรัฐประศาสนศาษตร์'), ('สังคมวิทยาและมานุษยวิทยา', 'สังคมวิทยาและมานุษยวิทยา'), ('โครงการสหวิทยาการระดับบัณฑิตศึกษา สาขาพัฒนาสังคม', 'โครงการสหวิทยาการระดับบัณฑิตศึกษา สาขาพัฒนาสังคม'), ('โครงการเอเชียตะวันออกเฉียงใต้ภาคพิเศษ', 'โครงการเอเชียตะวันออกเฉียงใต้ภาคพิเศษ'), ('กายวิภาคศาสตร์', 'กายวิภาคศาสตร์'), ('สรีรวิทยา', 'สรีรวิทยา'), ('จุลชีววิทยาและวิทยาภูมิคุ้มกัน', 'จุลชีววิทยาและวิทยาภูมิคุ้มกัน'), ('เภสัชวิทยา', 'เภสัชวิทยา'), ('พยาธิวิทยา', 'พยาธิวิทยา'), ('ปรสิตวิทยา', 'ปรสิตวิทยา'), ('เทคโนโลยีอุตสาหกรรมเกษตร', 'เทคโนโลยีอุตสาหกรรมเกษตร'), ('เทคโนโลยีชีวภาพ', 'เทคโนโลยีชีวภาพ'), ('วิทยาศาสตร์และเทคโนโลยีการอาหาร', 'วิทยาศาสตร์และเทคโนโลยีการอาหาร'), ('เทคโนโลยีการบรรจุ และวัสดุ', 'เทคโนโลยีการบรรจุ และวัสดุ'), ('พัฒนาผลิตภัณฑ์', 'พัฒนาผลิตภัณฑ์'), ('วิทยาการสิ่งทอ', 'วิทยาการสิ่งทอ'), ('นวัตกรรมและเทคโนโลยีอุตสาหกรรมเกษตร (หลักสูตรนานาชาติ)', 'นวัตกรรมและเทคโนโลยีอุตสาหกรรมเกษตร (หลักสูตรนานาชาติ)'), ('เทคนิคการสัตวแพทย์', 'เทคนิคการสัตวแพทย์'), ('สาขาวิชาการพยาบาลสัตว์ (ภาคพิเศษ)', 'สาขาวิชาการพยาบาลสัตว์ (ภาคพิเศษ)'), ('สาขาวิชาเทคนิคการสัตวแพทย์ (ภาคพิเศษ)', 'สาขาวิชาเทคนิคการสัตวแพทย์ (ภาคพิเศษ)'), ('เทคโนโลยีและการจัดการสิ่งแวดล้อม', 'เทคโนโลยีและการจัดการสิ่งแวดล้อม'), ('วิทยาศาสตร์สิ่งแวดล้อม', 'วิทยาศาสตร์สิ่งแวดล้อม'), ('แพทยศาสตร์', 'แพทยศาสตร์'), ('พยาบาลศาสตร์', 'พยาบาลศาสตร์'), ('การจัดการท่องเที่ยวเชิงวัฒนธรรมและสุขภาพ', 'การจัดการท่องเที่ยวเชิงวัฒนธรรมและสุขภาพ'), ('การจัดการอุตสาหกรรมการบริการ', 'การจัดการอุตสาหกรรมการบริการ')], max_length=150),
        ),
        migrations.AlterField(
            model_name='education',
            name='education_level',
            field=models.CharField(choices=[('ปริญญาตรี', 'ปริญญาตรี'), ('ปริญญาโท', 'ปริญญาโท'), ('ปริญญาเอก', 'ปริญญาเอก')], max_length=150),
        ),
        migrations.AlterField(
            model_name='education',
            name='faculty',
            field=models.CharField(choices=[('เกษตร', 'เกษตร'), ('บริหารธุรกิจ', 'บริหารธุรกิจ'), ('ประมง', 'ประมง'), ('มนุษยศาสตร์', 'มนุษยศาสตร์'), ('วนศาสตร์', 'วนศาสตร์'), ('วิทยาศาสตร์', 'วิทยาศาสตร์'), ('วิศวกรรมศาสตร์', 'วิศวกรรมศาสตร์'), ('ศึกษาศาสตร์', 'ศึกษาศาสตร์'), ('เศรษฐศาสตร์', 'เศรษฐศาสตร์'), ('สถาปัตยกรรมศาสตร์', 'สถาปัตยกรรมศาสตร์'), ('สังคมศาสตร์', 'สังคมศาสตร์'), ('สัตวแพทยศาสตร์', 'สัตวแพทยศาสตร์'), ('อุตสาหกรรมเกษตร', 'อุตสาหกรรมเกษตร'), ('เทคนิคการสัตวแพทย์', 'เทคนิคการสัตวแพทย์'), ('สิ่งแวดล้อม', 'สิ่งแวดล้อม'), ('แพทยศาสตร์', 'แพทยศาสตร์'), ('พยาบาลศาสตร์', 'พยาบาลศาสตร์'), ('สหวิทยาการจัดการและเทคโนโลยี', 'สหวิทยาการจัดการและเทคโนโลยี'), ('วิทยาลัยบูรณาการศาสตร์', 'วิทยาลัยบูรณาการศาสตร์'), ('บัณฑิตวิทยาลัย', 'บัณฑิตวิทยาลัย'), ('โครงการจัดตั้งวิทยาลัยนานาชาติ', 'โครงการจัดตั้งวิทยาลัยนานาชาติ')], max_length=150),
        ),
        migrations.AlterField(
            model_name='education',
            name='status',
            field=models.CharField(choices=[('ผู้กู้ยืมรายใหม่', 'ผู้กู้ยืมรายใหม่'), ('ผู้กู้ยืมรายเก่า', 'ผู้กู้ยืมรายเก่า')], default='NEW_BORROWER', max_length=150),
        ),
    ]
