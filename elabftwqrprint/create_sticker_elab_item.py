import argparse
import os
from . import _global_defaults as gconf
from . import _elabftw_interface as elabqr


def main():
    conf_path = os.path.expanduser(gconf.CONFIG_FOLDER)
    if not os.path.isdir(conf_path):
        os.mkdir(conf_path)
    default_path = conf_path+"/last_sticker.png"
    parser = argparse.ArgumentParser()
    parser.add_argument("id_no", type=str,
                        help="Database item to create QR-sticker for")
    parser.add_argument("-o", "--output", type=str,
                        help="Path to output file",
                        default=default_path)
    parser.add_argument("-l", "--long", type=str,
                        help="Long text to print next to QR code",
                        default=gconf.LONG_TEXT)
    parser.add_argument("-d", "--font_path", type=str,
                        help="Path to font file",
                        default=gconf.FONT)
    parser.add_argument("-f", "--fontsize", type=int,
                        help="Font size of small and big text",
                        default=gconf.FONT_SIZE)
    parser.add_argument("-s", "--qrsize", type=int,
                        help="Final print size of the QR-code in pixels",
                        default=None)
    p = parser.parse_args()
    elabqr.make_qrcode_item(p.id_no, p.output, long_text=p.long,
                            font_size=p.fontsize, font_path=p.font_path,
                            qr_size=p.qrsize)
    print(f"Created QR sticker for item {p.id_no} at {default_path}")


if __name__ == "__main__":
    main()
