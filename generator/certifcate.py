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
    # Open the Base certificate image
    img = Image.open(path)  # Replace with your base certificate image name
    # Make the image drawable
    d = ImageDraw.Draw(img)
    # Save all the information we are going to use
    text_color = (50, 50, 50)  # Replace with the color you want the text to be
    
    #location_course = (334, 250)
    location_course = (440, 250)  # Replace with the coordinates you noted. (X, Y)

    # location_name = (440, 390) 
    location_name = (350, 395) # Replace with the coordinates you noted. (X, Y)

    # location_date = (xxx, yyy) 
    location_date = (215, 485) # Replace with the coordinates you noted. (X, Y)
    
    # font1 = ImageFont.truetype(os.path.join(base_dir,"assets/fonts/font1.ttf"), 50)
    font1 = ImageFont.truetype(os.path.join(base_dir,"assets/fonts/font1.ttf"), 50) 

    # font2 = ImageFont.truetype(os.path.join(base_dir,"assets/fonts/font1.ttf"), 50)
    font2 = ImageFont.truetype(os.path.join(base_dir,"assets/fonts/font1.ttf"), 50) 

    # font3 = ImageFont.truetype(os.path.join(base_dir,"assets/fonts/font1.ttf"), 45)
    font3 = ImageFont.truetype(os.path.join(base_dir,"assets/fonts/font1.ttf"), 45) 
    
    
    # d.text(location_date, date, fill=text_color, font=font1)
    d.text(location_name, name, fill=text_color, font=font1)

    # d.text(location_course, course, fill=text_color, font=font2)
    d.text(location_course, course, fill=text_color, font=font2)

    # d.text(location_date, date, fill=text_color, font=font3)
    d.text(location_date, date, fill=text_color, font=font3)
    

    # Create a unique name for the file. Feel free to edit the format, this is an example
    file_name = os.path.join(base_dir+"/assets/generated/") +  "_".join(name.split(' ')) + str(random.randint(0, 255)) + ".png"
    # Save the image
    img.show()
    # img.save(file_name)
    # Return the name we generated
    return file_name

if __name__ == "__main__":
    write_name("Core Java", "Raju Prakash Pant", "09-11-2001")