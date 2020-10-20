# COVID-RIVM-script
Get notified when new number of COVID-19 tests is made available by Dutch RIVM before the news notifies you. It's a quick-and-dirty attempt to be made aware of new statistics, so please don't expect the most beautiful code 😉

## Install
1. Ensure that you have Python 3.x installed on your machine.
2. Ensure that you have `playsound` installed: `pip install playsound`
3. Ensure that you have `pandas` installed: `pip install pandas`
4. Ensure that you have `requests` installed: `pip install requests`
5. Clone this repository.
6. Download an alarm MP3 file from e.g. https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203 and add it to the folder where you cloned the repository, as `alarm.mp3`.
7. Run the script: `python covid.py`. Be nice and only do so when it's likely that new numbers appear, say after 1.30PM Dutch time.
8. The script will automatically stop when new numbers get in and you will be notified by sound.

## License
[Apache 2.0 License](./LICENSE)