import cv2 

def quit_program():
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        return True
    return False

def load_img(file_name):
    img_grey = cv2.imread(file_name, 0)
    img_colored = cv2.imread(file_name)
    return (img_grey, img_colored)

def get_coodernates_face(path_haar_file, grey_img):
    face_cascade = cv2.CascadeClassifier(path_haar_file)
    faces = face_cascade.detectMultiScale(grey_img, 1.2, 5) 
    print(faces)
    return faces

def draw_rec(coor_init, coor_fish, img):
    cv2.rectangle(img,coor_init, coor_fish, (255,255,0), 10)

def main():
    grey, img = load_img("./img_input/pessoa.jpg")

    faces_coordenates = get_coodernates_face("./haars/haar_face_pessoa.xml", grey)

    for face in faces_coordenates:
        init_coord = (face[0],face[1])
        finish_coord = (face[0] + face[2], face[1] + face[3])
        draw_rec(init_coord, finish_coord, img)

    cv2.imwrite("./img_output/final.jpg", img)

main()
