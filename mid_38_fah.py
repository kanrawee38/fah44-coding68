{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOgEszF6ELiSZr5kkRPXAve",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kanrawee38/fah44-coding68/blob/main/mid_38_fah_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "LJ4CpXehYF4X"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZuccF3mvX2bD",
        "outputId": "de449dcf-8b1c-4f9a-b661-35ebac92d734"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "คุณชื่ออะไรคะไก่\n",
            "สวัสดีค่ะไก่!\n",
            "กรุณาใส่ตัวเลข 789\n",
            "positive odd\n",
            "Zero\n"
          ]
        }
      ],
      "source": [
        "name = input(\"คุณชื่ออะไรคะ\")\n",
        "print(\"สวัสดีค่ะ\"+name +\"!\")\n",
        "num = float(input(\"กรุณาใส่ตัวเลข \"))\n",
        "if num > 0:\n",
        "    if num % 2 == 0:\n",
        "        print(\"positive even\")\n",
        "    else:\n",
        "        print(\"positive odd\")\n",
        "if num < 0:\n",
        "    if num % 2 == 0:\n",
        "        print(\"negative even\")\n",
        "    else:\n",
        "        print(\"negative odd\")\n",
        "else:\n",
        "    print(\"Zero\")"
      ]
    }
  ]
}
