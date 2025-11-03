import os
from filter.bounding_box import bbox
from filter.config import HTV_BOX, NEWS_BOX, COMPARE_BOX, NEWS_60S_VIDEOS

def main():
    # Example usage of the imported classes and objects
    print("HTV Box Coordinates:")
    print(f"X: {HTV_BOX.BOX_X}, Y: {HTV_BOX.BOX_Y}, Width: {HTV_BOX.BOX_W}, Height: {HTV_BOX.BOX_H}")

    print("\nNews Box Coordinates:")
    print(f"X: {NEWS_BOX.BOX_X}, Y: {NEWS_BOX.BOX_Y}, Width: {NEWS_BOX.BOX_W}, Height: {NEWS_BOX.BOX_H}")

    print("\nCompare Box Coordinates:")
    print(f"X: {COMPARE_BOX.BOX_X}, Y: {COMPARE_BOX.BOX_Y}, Width: {COMPARE_BOX.BOX_W}, Height: {COMPARE_BOX.BOX_H}")

    print("\n60s News Videos:")
    for video in NEWS_60S_VIDEOS.video_list:
        print(video)

if __name__ == "__main__":
    main()