import os
def structure():
    a = "form_builder_chips_input | @ Bads | Form Builders | Flutter"
    a = a.split('|')
    a.reverse()
    print(a)
    
    newpath = 'C:\\Users\\Administrator\\PycharmProjects\\pythonProject1\\'
    for i in a:
        newpath = newpath + i + "\\"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            
def removing_hashtags():
    pass

def crop_title():
    a = "Don't put dots after folder name. Collect design related files only via Total Commander !!!.mp4"
    if '.mp4' in a:
        a = a.split(' ') # changing from str to lists (diving)
        del a[-1] #deleting .mp4
        print(a)

structure()
crop_title()