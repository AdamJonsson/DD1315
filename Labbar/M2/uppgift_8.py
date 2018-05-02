from skimage import data
import matplotlib.patches as patches
import matplotlib.pyplot as plt

cat = data.chelsea()

plt.imshow(cat)

ax = plt.subplot(111)
rectBlack = patches.Rectangle((0,0),100,300,linewidth=1,facecolor='#00000090'); ax.add_patch(rectBlack)
rectRed = patches.Rectangle((100,0),100,300,linewidth=1,facecolor='#ff000090'); ax.add_patch(rectRed)
rectGreen = patches.Rectangle((200,0),100,300,linewidth=1,facecolor='#00ff0090'); ax.add_patch(rectGreen)
rectBlue = patches.Rectangle((300,0),100,300,linewidth=1,facecolor='#0000ff90'); ax.add_patch(rectBlue)
plt.show()