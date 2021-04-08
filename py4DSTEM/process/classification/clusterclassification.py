{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def braggpeak_cluster_prep(pointlistarray, Qx, Qy, bins_x, bins_y, mask=False):\n",
    "    \"\"\"\n",
    "    Prepare an array of peak positions for cluster classification\n",
    "    Accepts:\n",
    "        pointlistarray       (PointListArray)\n",
    "        Qx                   (int) Dimension of the diffraction pattern from the datacube in the x direction\n",
    "        Qy                   (int) Dimension of the diffraction pattern from the datacube in the y direction\n",
    "        bins_x               (int) Bin width in the x direction - Qx/bins_x must be a whole number\n",
    "        bins_y               (int) Bin width in the y direction - Qy/bins_y must be a whole number\n",
    "        mask                 (Bool 2D array) True where you want the peaks to be added, false where you don't want peaks added\n",
    "                                             Best used if false positives are strong around a beamstop/ beamstop mask \n",
    "    Returns:\n",
    "        peak_data            (ndarray) 2D array where the x dimension is the number of patterns and the y dimension is the intensity\n",
    "                                             at the bin location\n",
    "    \"\"\"\n",
    "    ##Need to add input error checks here\n",
    "    \n",
    "    nx_bins = int(Qx / bins_x)\n",
    "    ny_bins = int(Qy / bins_y)\n",
    "    n_bins = nx_bins * ny_bins\n",
    "    \n",
    "    ##Intialize empty array\n",
    "    \n",
    "    peak_data = np.zeros((pointlistarray.shape[0], pointlistarray.shape[1], n_bins))\n",
    "    \n",
    "    for (Rx, Ry) in tqdmnd(pointlistarray.shape[0],pointlistarray.shape[1]):\n",
    "        pointlist = pointlistarray.get_pointlist(Rx,Ry)\n",
    "        if pointlist.data.shape[0] == 0:\n",
    "            continue\n",
    "        elif mask is not False:\n",
    "            binval_x = np.floor(pointlist.data[i][0] / bins_x)\n",
    "            binval_y = np.floor(pointlist.data[i][1] / bins_y)\n",
    "            final_binval = int((binval_y * nx_bins) + binval_x)\n",
    "            peak_data[Rx,Ry,final_binval] = pointlist.data[i][2]\n",
    "        else:\n",
    "            for i in range(pointlist.data.shape[0]):\n",
    "                if np.where(mask[np.round(pointlist.data[i][0]).astype(int),np.round(pointlist.data[i][1]).astype(int)] == True, True, False) == False:\n",
    "                    continue\n",
    "                else:\n",
    "                    binval_x = np.floor(pointlist.data[i][0] / bins_x)\n",
    "                    binval_y = np.floor(pointlist.data[i][1] / bins_y)\n",
    "                    final_binval = int((binval_y * nx_bins) + binval_x)\n",
    "                    peak_data[Rx,Ry,final_binval] = pointlist.data[i][2]\n",
    "    return peak_data\n",
    "\n",
    "def get_class_images(dc, labels):\n",
    "    \"\"\"\n",
    "    A function to create class images from labels output from sklearn cluster classification.\n",
    "    Accepts:\n",
    "    dc           (datacube)\n",
    "    labels       (ndarray) array shaped [Rx*Ry, 1] with labels at each index\n",
    "    \n",
    "    Returns:\n",
    "    class_images (ndarray) array shaped [Q_Nx, Q_Ny, n_labels] containing the average pattern of the class\n",
    "    class_bins   (ndarray) number of patterns in each class\n",
    "    \"\"\"\n",
    "    class_images = np.zeros((dc.data.shape[2], dc.data.shape[3], n_clusters))\n",
    "    class_bins = np.bincount(labels)\n",
    "    print(class_images.shape)\n",
    "    for x in range(dc.R_Nx):\n",
    "            class_images[:,:,labels[x]] += dc.data[x,0]\n",
    "    for n in range(np.max(labels)):\n",
    "        class_images[:,:,n] = class_images[:,:,n] / class_bins[n]\n",
    "    return class_images, class_bins"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
