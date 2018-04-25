# BlockchainAnalyzerWeb
Web page for Blockchain Analyzer

Website: 

### Cloning

```bash
git clone --recursive https://github.com/graft-project/BlockchainAnalyzerWeb.git
```

### Installation

```bash
sudo apt-get update
sudo apt-get install git python-pip gnuplot
```

Install Gnuplot.py from here: http://gnuplot-py.sourceforge.net/ #TODO: Add good instruction

```bash
pip install -r requirements.txt
```

### Starting

```bash
python run.py
```

Start without stdout:

```bash
nohup python run.py &> block_analyzer.log &
```

or

```
./run_page.sh
```
