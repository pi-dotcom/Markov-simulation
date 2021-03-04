import numpy as np
import cv2


TILE_SIZE = 32
OFS = 50

MARKET = """
TTTTTTTTTTTTTTTTTT
Tm..............mT
TT..S#..a#..d#..IT
Tf..s#..w#..B#..iT
TF..S#..b#..d#..IT
Tf..s#..a#..B#..iT
TF..S#..w#..d#..IT
Tm...............T
TT..Cg..Cg..Cg...T
E...##..##..##...T
E................T
TTTTTTTTTTTTTTGGTT
""".strip()


class SupermarketMap:
    """Visualizes the supermarket background"""

    def __init__(self, layout, tiles):
        """
        layout : a string with each character representing a tile
        tile   : a numpy array containing the tile image
        """
        self.tiles = tiles
        self.contents = [list(row) for row in layout.split("\n")]
        self.xsize = len(self.contents[0])
        self.ysize = len(self.contents)
        self.image = np.zeros(
            (self.ysize * TILE_SIZE, self.xsize * TILE_SIZE, 3), dtype=np.uint8
        )
        self.prepare_map()

    def get_tile(self, char):
        """returns the array for a given tile character"""
        tile_size = 32

        if char == "#":
            row_start = 0
            column_start = 0
            #return self.tiles[0:tile_size, 0:tile_size]
        elif char == "G":
            row_start = 7
            column_start = 3
            #return self.tiles[7 * tile_size : 8 * tile_size, 3 * tile_size : 4 * tile_size]
        elif char == "C":
            row_start = 2
            column_start = 8
            #return self.tiles[2 * tile_size : 3 * tile_size, 8 * tile_size : 9 * tile_size]
        elif char == "b":
            row_start = 0
            column_start = 4
            #return self.tiles[0 * tile_size : 1 * tile_size, 4 * tile_size : 5 * tile_size]
        elif char == "a":
            row_start = 5
            column_start = 5
        elif char == "p":
            row_start = 5
            column_start = 4
        elif char == "o":
            row_start = 1
            column_start = 4
        elif char == "w":
            row_start = 3
            column_start = 4
        elif char == "B":
            row_start = 6
            column_start = 13
        elif char == "D":
            row_start = 3
            column_start = 13
        elif char == "d":
            row_start = 4
            column_start = 9
        elif char == "i":
            row_start = 2
            column_start = 12
        elif char == "I":
            row_start = 6
            column_start = 12
        elif char == "S":
            row_start = 0
            column_start = 3
        elif char == "s":
            row_start = 1
            column_start = 3
        elif char == "f":
            row_start = 6
            column_start = 15
        elif char == "F":
            row_start = 0
            column_start = 14
        elif char == "E":
            row_start = 6
            column_start = 10
        elif char == "m":
            row_start = 4
            column_start = 3
        elif char == "g":
            row_start = 7
            column_start = 2
        elif char == "T":
            row_start = 1
            column_start = 1
        
        
        else:
            row_start = 1
            column_start = 2
            # return self.tiles[32:64, 64:96]
        return self.tiles[row_start * tile_size : (row_start+1) * tile_size, column_start * tile_size : (column_start+1) * tile_size]

    def prepare_map(self):
        """prepares the entire image as a big numpy array"""
        for y, row in enumerate(self.contents):
            for x, tile in enumerate(row):
                bm = self.get_tile(tile)
                self.image[
                    y * TILE_SIZE : (y + 1) * TILE_SIZE,
                    x * TILE_SIZE : (x + 1) * TILE_SIZE,
                ] = bm

    def draw(self, frame, offset=OFS):
        """
        draws the image into a frame
        offset pixels from the top left corner
        """
        frame[
            OFS : OFS + self.image.shape[0], OFS : OFS + self.image.shape[1]
        ] = self.image

    def write_image(self, filename):
        """writes the image into a file"""
        cv2.imwrite(filename, self.image)


if __name__ == "__main__":

    background = np.zeros((700, 1000, 3), np.uint8)
    tiles = cv2.imread("tiles.png")

    market = SupermarketMap(MARKET, tiles)

    while True:
        frame = background.copy()
        market.draw(frame)

        cv2.imshow("frame", frame)

        key = chr(cv2.waitKey(1) & 0xFF)
        if key == "q":
            break

    cv2.destroyAllWindows()

    market.write_image("supermarket.png")
