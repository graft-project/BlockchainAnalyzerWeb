from flask import Blueprint, render_template, url_for, request
from flask_website.listings.releases import releases
from DAAAnalysis.DAAAnalysis.daemon_data import get_mainnet_blockchain_height
from DAAAnalysis.DAAAnalysis.update_block_data import update_block_data
from DAAAnalysis.DAAAnalysis.config import LOCAL_DAEMON_ADDRESS_MAINNET
from DAAAnalysis.DAAAnalysis.daa_analysis import analyze
import os

mod = Blueprint('general', __name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
BLOCK_WINDOW = 3000

BLOCKCHAIN_DATA = os.path.join(APP_ROOT, "..", "..", "DAAAnalysis", "DAAAnalysis", "blockdata", "mainnet_blocks.csv")
IMAGE_DATA = os.path.join(APP_ROOT, "..", "static", "charts")
if not os.path.exists(IMAGE_DATA):
    os.mkdir(IMAGE_DATA)


@mod.route('/')
def index(min_value=0, max_value=0):
    update_block_data(BLOCKCHAIN_DATA, LOCAL_DAEMON_ADDRESS_MAINNET)
    min_value = min_value if min_value > 0 else blockchain_height() - BLOCK_WINDOW
    max_value = max_value if max_value > 0 is not None else blockchain_height()
    chart_paths = []
    error_message = ""
    if min_value < max_value:
        chart_paths = analyze(min_value, max_value,
                              read_csv_file=BLOCKCHAIN_DATA, save_images=True,
                              save_image_path=IMAGE_DATA, single_image=True)
    else:
        error_message = "Block range isn't valid. Please, enter valid block range."

    return render_template(
        'general/index.html',
        latest_release=releases[-1],
        # pdf link does not redirect, needs version
        # docs version only includes major.minor
        docs_pdf_version='.'.join(releases[-1].version.split('.', 2)[:2]),
        difficulty_chart=difficulty_chart,
        blockchain_height=blockchain_height,
        minimum_value=min_value,
        maximum_value=max_value,
        last_error=error_message
    )


def difficulty_chart():
    return url_for('static', filename='charts/chart_0.svg')


def blockchain_height():
    height = get_mainnet_blockchain_height()
    return height


@mod.route('/store_data', methods=['POST'])
def store_data():
    curr_min_value = request.form['min_input']
    curr_max_value = request.form['max_input']
    return index(int(curr_min_value), int(curr_max_value))
