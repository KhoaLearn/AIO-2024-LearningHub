from background_subtraction import BackgroundSubtraction
import cv2
import matplotlib.pyplot as plt

def plot_images(images, titles, save_path=None):
    fig, axes = plt.subplots(2, 3)

    for i, (img, title) in enumerate(zip(images, titles)):
        row, col = i // 3, i % 3
        axes[row, col].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        axes[row, col].set_title(title)
        axes[row, col].axis('off')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)

    plt.show()

import os

def check_file_exists(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")

if __name__ == '__main__':
    bg_subtractor = BackgroundSubtraction(data_folder='/Users/datarist/AIO-2024-LearningHub/module2/week2_vector/code/Image data')
    
    # Check if files exist before attempting to load them
    check_file_exists(os.path.join(bg_subtractor.data_folder, 'GreenBackground.png'))
    check_file_exists(os.path.join(bg_subtractor.data_folder, 'NewBackground.jpg'))
    check_file_exists(os.path.join(bg_subtractor.data_folder, 'Object.png'))
    
    bg_subtractor.store_images('GreenBackground.png', 'NewBackground.jpg', 'Object.png')

    orig_bg_img, target_bg_img, ob_img = bg_subtractor.bg1_image, bg_subtractor.bg2_image, bg_subtractor.ob_image

    diff_image = bg_subtractor.compute_difference(orig_bg_img, ob_img)
    binary_mask = bg_subtractor.compute_binary_mask(diff_image)
    output_img = bg_subtractor.replace_background()
    images = [orig_bg_img, target_bg_img, ob_img, diff_image, binary_mask, output_img]
    titles = ['Original Background', 'Target Background', 'Object', 'Foreground Mask', 'Segmented Object', 'Final Output']

    plot_images(images, titles, '/Users/datarist/AIO-2024-LearningHub/module2/week2_vector/code/Image data/output.png')
