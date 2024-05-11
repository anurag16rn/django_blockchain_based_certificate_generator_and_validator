# utils.py
from PIL import Image, ImageDraw, ImageFont
import random
import os

def write_name(
        course: str,
        name: str,
        date:str,
        template = 'template_1.jpg'
    ) -> str:
    base_dir = os.getcwd()
    
    path = os.path.join(base_dir,"assets/certificate/"+template)
      
    # font1 = ImageFont.truetype(os.path.join(base_dir,"assets/fonts/font1.ttf"), 50)
    font1 = ImageFont.truetype(os.path.join(base_dir,"assets/fonts/ARIAL.ttf"), 35) 

    # font2 = ImageFont.truetype(os.path.join(base_dir,"assets/fonts/font1.ttf"), 50)
    font2 = ImageFont.truetype(os.path.join(base_dir,"assets/fonts/font1.ttf"), 50) 

    # font3 = ImageFont.truetype(os.path.join(base_dir,"assets/fonts/font1.ttf"), 45)
    font3 = ImageFont.truetype(os.path.join(base_dir,"assets/fonts/ARIAL.ttf"), 30) 
    
    # Open the Base certificate image
    img = Image.open(path)  # Replace with your base certificate image name
    # Make the image drawable
    d = ImageDraw.Draw(img)
    # Save all the information we are going to use
    text_color = (50, 50, 50)  # Replace with the color you want the text to be
    course_sz = d.textlength(course, font=font1)
    name_sz = d.textlength(name, font=font2)
    date_sz = d.textlength(date, font=font3)
    #location_course = (xxx, yyy)
    course_center = (img.width - course_sz) / 2
    location_course = (course_center, 420)  # Replace with the coordinates you noted. (X, Y)

    # location_name = (xxx, yyy)
    name_center = (img.width - name_sz) / 2
    location_name = (name_center, 620) # Replace with the coordinates you noted. (X, Y)

    # location_date = (xxx, yyy) 
    location_date = (380, 760) # Replace with the coordinates you noted. (X, Y)
  
    
    # d.text(location_course, course, fill=text_color, font=font1)
    d.text(location_course, course, fill=text_color, font=font1, align='center')

    # d.text(location_name, name, fill=text_color, font=font2)
    d.text(location_name, name, fill=text_color, font=font2, align='center')

    # d.text(location_date, date, fill=text_color, font=font3)
    d.text(location_date, date, fill=text_color, font=font3, align='center')
    

    # Create a unique name for the file. Feel free to edit the format, this is an example
    file_name = os.path.join(base_dir+"/assets/generated/") +  "_".join(name.split(' ')) + str(random.randint(0, 255)) + ".png"
    # Save the image
    img.show()
    # img.save(file_name)
    # Return the name we generated
    return file_name

if __name__ == "__main__":
    write_name("Core Java", "Roait Jaiswal", "10-05-2024")