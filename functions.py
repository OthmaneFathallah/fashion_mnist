import matplotlib.pyplot as plt

def display_images(images, labels, class_names):
    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i])
        plt.xlabel(f'Label {labels[i]}:{class_names[labels[i]]}')
    plt.show()