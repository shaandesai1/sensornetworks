import os
import pandas as pd
import numpy as np
import progressbar
import time
import q4functions as q4funcs


def predict(train, test, n_ap):
    pass


def get_training_data(path, calculate_means_and_variances=True):
    ''' Loads in training data from path argument, and returns in matrix for with mac addresses as columns.
        If calculate_means_and_variances=True the entries are the means and standard deviations of the readings,
        else just a list of all samples is returned
    '''
    print(f'Loading training data from {path}')
    time.sleep(0.2)
    locations_df = pd.read_csv(os.path.join(path, 'location.txt'), header=None)
    locations_df.columns = ['x', 'y']
    features_path = os.path.join(path, 'wifi_signal')
    feature_csvs = os.listdir(features_path)
    train_df = pd.DataFrame()
    for feature_csv in progressbar.progressbar(feature_csvs, prefix=f'Loading training data from {path}'):
        location = np.array(locations_df.iloc[int(feature_csv[6:].split('.')[0]) - 1])
        #         corresponding_location = locations_df[]
        feature_df = pd.read_csv(os.path.join(features_path, feature_csv), header=None)
        feature_df.columns = ['timestamp', 'router_name', 'mac_address', 'channel', 'RSSI']
        unique_mac_addresses = list(set(feature_df['mac_address']))
        location_dict = {'x': location[0], 'y': location[1]}

        for unique_mac_address in unique_mac_addresses:
            relevant_entries = feature_df.iloc[np.where(feature_df['mac_address'] == unique_mac_address)]
            rssi_values = relevant_entries['RSSI'] + 0.5 * np.random.random(size=len(relevant_entries))
            if calculate_means_and_variances:
                #             add artificial noise to avoid 0 standard deviation
                mean = rssi_values.mean()
                std_dv = rssi_values.std()
                means_and_stdevs = [mean, std_dv]
                location_dict[unique_mac_address] = means_and_stdevs
            else:
                location_dict[unique_mac_address] = rssi_values
        train_df = train_df.append(location_dict, ignore_index=True)
    train_df = train_df.reindex(columns=['x', 'y'] + [col for col in train_df.columns if col not in ['x', 'y']])
    return train_df


def get_test_data(path):
    locations_df = pd.read_csv(os.path.join(path, 'location.txt'), header=None)
    features_path = os.path.join(path, 'wifi_signal')
    feature_csvs = os.listdir(features_path)
    test_df = pd.DataFrame()
    for feature_csv in feature_csvs:

        feature_df = pd.read_csv(os.path.join(features_path, feature_csv))
        feature_df.columns = ['timestamp', 'router_name', 'mac_address', 'channel', 'RSSI']
        unique_mac_addresses = list(set(feature_df['mac_address']))
        location_dict = {'x': 0, 'y': 0}

        for unique_mac_address in unique_mac_addresses:
            relevant_entries = feature_df.iloc[np.where(feature_df['mac_address'] == unique_mac_address)]
            rssi_values = relevant_entries['RSSI']
            location_dict[unique_mac_address] = rssi_values
        test_df = test_df.append(location_dict, ignore_index=True)
    test_df = test_df.reindex(columns=['x', 'y'] + [col for col in test_df.columns if col not in ['x', 'y']])
    return test_df


def make_predictions(train_data, test_data):
    locations = []
    for i in range(len(test_data)):
        test_features = pd.DataFrame(test_data.iloc[i]).transpose()
        test_mac_addresses = set(test_features.columns[2:])
        train_mac_addresses = set(train_data.columns[2:])
        mutual_mac_addresses = list(test_mac_addresses.intersection(train_mac_addresses))
        cropped_test_df = test_features[['x', 'y'] + mutual_mac_addresses]

        cropped_test_df = pd.DataFrame(cropped_test_df.apply(lambda x: np.mean(x[0]))).transpose()
        cropped_train_df = train_data[['x', 'y'] + mutual_mac_addresses]

        _, location = q4funcs.predict(cropped_train_df.values, cropped_test_df.values, len(cropped_test_df.columns[2:]))
        print(location)
        locations.append(location)

    print(locations)
    return cropped_test_df, cropped_train_df


def preprocess_training_data(*args):
    pass


training_path = "./real_data/training/"
test_path = "./real_data/test/"

# get_training_data(training_path,calculate_means_and_variances=True).head()
test_data = get_test_data(test_path)
train_data = get_training_data(training_path)

a, b = make_predictions(train_data, test_data)


# b = b.values