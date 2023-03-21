{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "bfe5ec00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.87301462 2.11179688]\n"
     ]
    }
   ],
   "source": [
    "#### This sample code was auto-generated using Bing's ChatGPT AI (GPT-4).\n",
    "\n",
    "import numpy as np\n",
    "from scipy import optimize\n",
    "\n",
    "# Define the function that we want to fit\n",
    "def test_func(x, a, b):\n",
    "    return a * np.sin(b * x)\n",
    "\n",
    "# Generate some data with noise to fit\n",
    "x_data = np.linspace(0, 4 * np.pi, 100)\n",
    "y_data = 9.0 * np.sin(1.5 * x_data) + 0.5 * np.random.normal(size=100)\n",
    "\n",
    "# Fit the data with the function\n",
    "params, params_covariance = optimize.curve_fit(test_func, x_data, y_data, p0=[2, 2])\n",
    "\n",
    "# Print the results\n",
    "print(params)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5b589b5e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dc24dd46419c4d389e61b5c2b5479444",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Map(center=[24.9677, 121.187], controls=(ZoomControl(options=['position', 'zoom_in_text', 'zoom_in_title', 'zo…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#### This sample code was modified from ipyleaflet's demo examples.\n",
    "from ipyleaflet import Map, basemaps, basemap_to_tiles, Marker\n",
    "\n",
    "center = (24.9677, 121.1870)\n",
    "\n",
    "m = Map(\n",
    "    basemap=basemap_to_tiles(basemaps.OpenStreetMap.Mapnik),\n",
    "    center=center,\n",
    "    zoom=15\n",
    "    )\n",
    "marker = Marker(location=center, draggable=False)\n",
    "m.add_layer(marker);\n",
    "m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ac9eb183",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting ipyleaflet\n",
      "  Downloading ipyleaflet-0.17.2-py3-none-any.whl (3.7 MB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.7/3.7 MB\u001b[0m \u001b[31m10.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: branca>=0.5.0 in /opt/conda/lib/python3.10/site-packages (from ipyleaflet) (0.6.0)\n",
      "Requirement already satisfied: xyzservices>=2021.8.1 in /opt/conda/lib/python3.10/site-packages (from ipyleaflet) (2022.9.0)\n",
      "Collecting traittypes<3,>=0.2.1\n",
      "  Downloading traittypes-0.2.1-py2.py3-none-any.whl (8.6 kB)\n",
      "Requirement already satisfied: ipywidgets<9,>=7.6.0 in /opt/conda/lib/python3.10/site-packages (from ipyleaflet) (7.7.2)\n",
      "Requirement already satisfied: jinja2 in /opt/conda/lib/python3.10/site-packages (from branca>=0.5.0->ipyleaflet) (3.1.2)\n",
      "Requirement already satisfied: ipykernel>=4.5.1 in /opt/conda/lib/python3.10/site-packages (from ipywidgets<9,>=7.6.0->ipyleaflet) (6.19.2)\n",
      "Requirement already satisfied: ipython-genutils~=0.2.0 in /opt/conda/lib/python3.10/site-packages (from ipywidgets<9,>=7.6.0->ipyleaflet) (0.2.0)\n",
      "Requirement already satisfied: ipython>=4.0.0 in /opt/conda/lib/python3.10/site-packages (from ipywidgets<9,>=7.6.0->ipyleaflet) (8.7.0)\n",
      "Requirement already satisfied: traitlets>=4.3.1 in /opt/conda/lib/python3.10/site-packages (from ipywidgets<9,>=7.6.0->ipyleaflet) (5.7.1)\n",
      "Requirement already satisfied: widgetsnbextension~=3.6.0 in /opt/conda/lib/python3.10/site-packages (from ipywidgets<9,>=7.6.0->ipyleaflet) (3.6.1)\n",
      "Requirement already satisfied: jupyterlab-widgets<3,>=1.0.0 in /opt/conda/lib/python3.10/site-packages (from ipywidgets<9,>=7.6.0->ipyleaflet) (1.1.1)\n",
      "Requirement already satisfied: pyzmq>=17 in /opt/conda/lib/python3.10/site-packages (from ipykernel>=4.5.1->ipywidgets<9,>=7.6.0->ipyleaflet) (24.0.1)\n",
      "Requirement already satisfied: comm>=0.1.1 in /opt/conda/lib/python3.10/site-packages (from ipykernel>=4.5.1->ipywidgets<9,>=7.6.0->ipyleaflet) (0.1.2)\n",
      "Requirement already satisfied: matplotlib-inline>=0.1 in /opt/conda/lib/python3.10/site-packages (from ipykernel>=4.5.1->ipywidgets<9,>=7.6.0->ipyleaflet) (0.1.6)\n",
      "Requirement already satisfied: packaging in /opt/conda/lib/python3.10/site-packages (from ipykernel>=4.5.1->ipywidgets<9,>=7.6.0->ipyleaflet) (22.0)\n",
      "Requirement already satisfied: debugpy>=1.0 in /opt/conda/lib/python3.10/site-packages (from ipykernel>=4.5.1->ipywidgets<9,>=7.6.0->ipyleaflet) (1.6.4)\n",
      "Requirement already satisfied: nest-asyncio in /opt/conda/lib/python3.10/site-packages (from ipykernel>=4.5.1->ipywidgets<9,>=7.6.0->ipyleaflet) (1.5.6)\n",
      "Requirement already satisfied: tornado>=6.1 in /opt/conda/lib/python3.10/site-packages (from ipykernel>=4.5.1->ipywidgets<9,>=7.6.0->ipyleaflet) (6.1)\n",
      "Requirement already satisfied: psutil in /opt/conda/lib/python3.10/site-packages (from ipykernel>=4.5.1->ipywidgets<9,>=7.6.0->ipyleaflet) (5.9.4)\n",
      "Requirement already satisfied: jupyter-client>=6.1.12 in /opt/conda/lib/python3.10/site-packages (from ipykernel>=4.5.1->ipywidgets<9,>=7.6.0->ipyleaflet) (7.3.4)\n",
      "Requirement already satisfied: stack-data in /opt/conda/lib/python3.10/site-packages (from ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.6.2)\n",
      "Requirement already satisfied: pickleshare in /opt/conda/lib/python3.10/site-packages (from ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.7.5)\n",
      "Requirement already satisfied: decorator in /opt/conda/lib/python3.10/site-packages (from ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (5.1.1)\n",
      "Requirement already satisfied: jedi>=0.16 in /opt/conda/lib/python3.10/site-packages (from ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.18.2)\n",
      "Requirement already satisfied: pexpect>4.3 in /opt/conda/lib/python3.10/site-packages (from ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (4.8.0)\n",
      "Requirement already satisfied: prompt-toolkit<3.1.0,>=3.0.11 in /opt/conda/lib/python3.10/site-packages (from ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (3.0.36)\n",
      "Requirement already satisfied: backcall in /opt/conda/lib/python3.10/site-packages (from ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.2.0)\n",
      "Requirement already satisfied: pygments>=2.4.0 in /opt/conda/lib/python3.10/site-packages (from ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (2.13.0)\n",
      "Requirement already satisfied: notebook>=4.4.1 in /opt/conda/lib/python3.10/site-packages (from widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (6.5.2)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /opt/conda/lib/python3.10/site-packages (from jinja2->branca>=0.5.0->ipyleaflet) (2.1.1)\n",
      "Requirement already satisfied: parso<0.9.0,>=0.8.0 in /opt/conda/lib/python3.10/site-packages (from jedi>=0.16->ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.8.3)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /opt/conda/lib/python3.10/site-packages (from jupyter-client>=6.1.12->ipykernel>=4.5.1->ipywidgets<9,>=7.6.0->ipyleaflet) (2.8.2)\n",
      "Requirement already satisfied: entrypoints in /opt/conda/lib/python3.10/site-packages (from jupyter-client>=6.1.12->ipykernel>=4.5.1->ipywidgets<9,>=7.6.0->ipyleaflet) (0.4)\n",
      "Requirement already satisfied: jupyter-core>=4.9.2 in /opt/conda/lib/python3.10/site-packages (from jupyter-client>=6.1.12->ipykernel>=4.5.1->ipywidgets<9,>=7.6.0->ipyleaflet) (5.1.0)\n",
      "Requirement already satisfied: nbformat in /opt/conda/lib/python3.10/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (5.7.0)\n",
      "Requirement already satisfied: Send2Trash>=1.8.0 in /opt/conda/lib/python3.10/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (1.8.0)\n",
      "Requirement already satisfied: terminado>=0.8.3 in /opt/conda/lib/python3.10/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.17.1)\n",
      "Requirement already satisfied: prometheus-client in /opt/conda/lib/python3.10/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.15.0)\n",
      "Requirement already satisfied: argon2-cffi in /opt/conda/lib/python3.10/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (21.3.0)\n",
      "Requirement already satisfied: nbclassic>=0.4.7 in /opt/conda/lib/python3.10/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.4.8)\n",
      "Requirement already satisfied: nbconvert>=5 in /opt/conda/lib/python3.10/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (7.2.6)\n",
      "Requirement already satisfied: ptyprocess>=0.5 in /opt/conda/lib/python3.10/site-packages (from pexpect>4.3->ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.7.0)\n",
      "Requirement already satisfied: wcwidth in /opt/conda/lib/python3.10/site-packages (from prompt-toolkit<3.1.0,>=3.0.11->ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.2.5)\n",
      "Requirement already satisfied: asttokens>=2.1.0 in /opt/conda/lib/python3.10/site-packages (from stack-data->ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (2.2.1)\n",
      "Requirement already satisfied: executing>=1.2.0 in /opt/conda/lib/python3.10/site-packages (from stack-data->ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (1.2.0)\n",
      "Requirement already satisfied: pure-eval in /opt/conda/lib/python3.10/site-packages (from stack-data->ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.2.2)\n",
      "Requirement already satisfied: six in /opt/conda/lib/python3.10/site-packages (from asttokens>=2.1.0->stack-data->ipython>=4.0.0->ipywidgets<9,>=7.6.0->ipyleaflet) (1.16.0)\n",
      "Requirement already satisfied: platformdirs>=2.5 in /opt/conda/lib/python3.10/site-packages (from jupyter-core>=4.9.2->jupyter-client>=6.1.12->ipykernel>=4.5.1->ipywidgets<9,>=7.6.0->ipyleaflet) (2.6.0)\n",
      "Requirement already satisfied: notebook-shim>=0.1.0 in /opt/conda/lib/python3.10/site-packages (from nbclassic>=0.4.7->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.2.2)\n",
      "Requirement already satisfied: jupyter-server>=1.8 in /opt/conda/lib/python3.10/site-packages (from nbclassic>=0.4.7->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (1.23.3)\n",
      "Requirement already satisfied: bleach in /opt/conda/lib/python3.10/site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (5.0.1)\n",
      "Requirement already satisfied: mistune<3,>=2.0.3 in /opt/conda/lib/python3.10/site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (2.0.4)\n",
      "Requirement already satisfied: tinycss2 in /opt/conda/lib/python3.10/site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (1.2.1)\n",
      "Requirement already satisfied: beautifulsoup4 in /opt/conda/lib/python3.10/site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (4.11.1)\n",
      "Requirement already satisfied: jupyterlab-pygments in /opt/conda/lib/python3.10/site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.2.2)\n",
      "Requirement already satisfied: pandocfilters>=1.4.1 in /opt/conda/lib/python3.10/site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (1.5.0)\n",
      "Requirement already satisfied: nbclient>=0.5.0 in /opt/conda/lib/python3.10/site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.7.2)\n",
      "Requirement already satisfied: defusedxml in /opt/conda/lib/python3.10/site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.7.1)\n",
      "Requirement already satisfied: jsonschema>=2.6 in /opt/conda/lib/python3.10/site-packages (from nbformat->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (4.17.3)\n",
      "Requirement already satisfied: fastjsonschema in /opt/conda/lib/python3.10/site-packages (from nbformat->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (2.16.2)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: argon2-cffi-bindings in /opt/conda/lib/python3.10/site-packages (from argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (21.2.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /opt/conda/lib/python3.10/site-packages (from jsonschema>=2.6->nbformat->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.19.2)\n",
      "Requirement already satisfied: attrs>=17.4.0 in /opt/conda/lib/python3.10/site-packages (from jsonschema>=2.6->nbformat->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (22.1.0)\n",
      "Requirement already satisfied: websocket-client in /opt/conda/lib/python3.10/site-packages (from jupyter-server>=1.8->nbclassic>=0.4.7->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (1.4.2)\n",
      "Requirement already satisfied: anyio<4,>=3.1.0 in /opt/conda/lib/python3.10/site-packages (from jupyter-server>=1.8->nbclassic>=0.4.7->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (3.6.2)\n",
      "Requirement already satisfied: cffi>=1.0.1 in /opt/conda/lib/python3.10/site-packages (from argon2-cffi-bindings->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (1.15.1)\n",
      "Requirement already satisfied: soupsieve>1.2 in /opt/conda/lib/python3.10/site-packages (from beautifulsoup4->nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (2.3.2.post1)\n",
      "Requirement already satisfied: webencodings in /opt/conda/lib/python3.10/site-packages (from bleach->nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (0.5.1)\n",
      "Requirement already satisfied: sniffio>=1.1 in /opt/conda/lib/python3.10/site-packages (from anyio<4,>=3.1.0->jupyter-server>=1.8->nbclassic>=0.4.7->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (1.3.0)\n",
      "Requirement already satisfied: idna>=2.8 in /opt/conda/lib/python3.10/site-packages (from anyio<4,>=3.1.0->jupyter-server>=1.8->nbclassic>=0.4.7->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (2.10)\n",
      "Requirement already satisfied: pycparser in /opt/conda/lib/python3.10/site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets<9,>=7.6.0->ipyleaflet) (2.21)\n",
      "Installing collected packages: traittypes, ipyleaflet\n",
      "Successfully installed ipyleaflet-0.17.2 traittypes-0.2.1\n"
     ]
    }
   ],
   "source": [
    "!pip install ipyleaflet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e614f0e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "447300c6837d411fad4d52274b4a7bf0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Map(center=[24.9677, 121.187], controls=(ZoomControl(options=['position', 'zoom_in_text', 'zoom_in_title', 'zo…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#### This sample code was modified from ipyleaflet's demo examples.\n",
    "from ipyleaflet import Map, basemaps, basemap_to_tiles, Marker\n",
    "\n",
    "center = (24.9677, 121.1870)\n",
    "\n",
    "m = Map(\n",
    "    basemap=basemap_to_tiles(basemaps.OpenStreetMap.Mapnik),\n",
    "    center=center,\n",
    "    zoom=15\n",
    "    )\n",
    "marker = Marker(location=center, draggable=False)\n",
    "m.add_layer(marker);\n",
    "m"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
