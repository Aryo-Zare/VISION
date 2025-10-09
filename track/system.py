
# os commands
    # editing file-names.
    # generating commands to execute Emil's preprrocessing steps : un-warping ( the fish-eye distortion ) & histogram equalization.

# %%'

# env_1

import os

# %%' rename

# replace spaces as they will be interpreted as a separate argument when running Emil's script directly from terminal.

def rename_files(directory):
    # Loop over all items in the specified directory
    for filename in os.listdir(directory):
        # Check if the current item is a file and contains spaces
        full_path = os.path.join(directory, filename)
        # check if the path is a file path & not a sub-direcoty path :
        if os.path.isfile(full_path) and ' ' in filename:
            # Replace spaces with underscores
            new_filename = filename.replace(' ', '_')
            new_full_path = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(full_path, new_full_path)
            print(f'Renamed: "{filename}" to "{new_filename}"')

# %%'

# Simply run the function at the bottom of your script:
directory = r'D:\video\pod_7'
rename_files(directory)

# %%'

# Renamed: "P067_ZC66_OF2ReTr Video 1 03_09_2023 10_56_43 1.mp4" to "P067_ZC66_OF2ReTr_Video_1_03_09_2023_10_56_43_1.mp4"
# Renamed: "P067_ZC67_OF2ReTr Video 1 11_09_2023 10_44_13 1.mp4" to "P067_ZC67_OF2ReTr_Video_1_11_09_2023_10_44_13_1.mp4"
# Renamed: "P067_ZC68_OF2ReTr Video 1 08_10_2023 10_48_19 1.mp4" to "P067_ZC68_OF2ReTr_Video_1_08_10_2023_10_48_19_1.mp4"
# Renamed: "ZC04_20200216 Video 2 2_16_2020 11_03_19 AM 1.mp4" to "ZC04_20200216_Video_2_2_16_2020_11_03_19_AM_1.mp4"

# %%'

# Renamed: "P067_ZC60_POD1 Video 1 06_06_2023 11_22_38 1.mp4" to "P067_ZC60_POD1_Video_1_06_06_2023_11_22_38_1.mp4"
# Renamed: "P067_ZC61_POD1 Video 1 30_06_2023 11_00_49 1.mp4" to "P067_ZC61_POD1_Video_1_30_06_2023_11_00_49_1.mp4"
# Renamed: "P067_ZC62_POD1 Video 1 06_07_2023 11_10_52 1.mp4" to "P067_ZC62_POD1_Video_1_06_07_2023_11_10_52_1.mp4"
# Renamed: "P067_ZC63_POD1 Video 1 25_07_2023 11_01_31 1.mp4" to "P067_ZC63_POD1_Video_1_25_07_2023_11_01_31_1.mp4"
# Renamed: "P067_ZC65_POD1 Video 1 08_08_2023 10_55_42 1.mp4" to "P067_ZC65_POD1_Video_1_08_08_2023_10_55_42_1.mp4"
# Renamed: "P067_ZC65_POD1 Video 1 08_08_2023 14_03_53 1.mp4" to "P067_ZC65_POD1_Video_1_08_08_2023_14_03_53_1.mp4"
# Renamed: "P067_ZC66_POD1 Video 1 05_09_2023 10_58_33 1.mp4" to "P067_ZC66_POD1_Video_1_05_09_2023_10_58_33_1.mp4"
# Renamed: "P067_ZC67_POD1 Video 1 13_09_2023 11_10_55 1.mp4" to "P067_ZC67_POD1_Video_1_13_09_2023_11_10_55_1.mp4"
# Renamed: "P067_ZC68_POD1 Video 1 10_10_2023 11_03_52 1.mp4" to "P067_ZC68_POD1_Video_1_10_10_2023_11_03_52_1.mp4"
# Renamed: "P067_ZC69_POD1 Video 1 24_10_2023 11_00_02 1.mp4" to "P067_ZC69_POD1_Video_1_24_10_2023_11_00_02_1.mp4"
# Renamed: "ZC04_20200219 Video 2 2_19_2020 11_11_14 AM 1.mp4" to "ZC04_20200219_Video_2_2_19_2020_11_11_14_AM_1.mp4"
# Renamed: "ZC05_20200312 Video 2 3_12_2020 11_03_19 AM 1.mp4" to "ZC05_20200312_Video_2_3_12_2020_11_03_19_AM_1.mp4"
# Renamed: "ZC06_20200312 Video 2 3_12_2020 11_18_50 AM 1.mp4" to "ZC06_20200312_Video_2_3_12_2020_11_18_50_AM_1.mp4"
# Renamed: "ZC07_20200610 Video 2 6_10_2020 11_00_34 AM 1.mp4" to "ZC07_20200610_Video_2_6_10_2020_11_00_34_AM_1.mp4"

# Renamed: "ZC05_20200309 Video 2 3_9_2020 11_10_13 AM 1.mp4" to "ZC05_20200309_Video_2_3_9_2020_11_10_13_AM_1.mp4"
# Renamed: "ZC06_20200309 Video 2 3_9_2020 11_34_04 AM 1.mp4" to "ZC06_20200309_Video_2_3_9_2020_11_34_04_AM_1.mp4"
# Renamed: "ZC07_20200607 Video 2 6_7_2020 10_59_59 AM 1.mp4" to "ZC07_20200607_Video_2_6_7_2020_10_59_59_AM_1.mp4"
# Renamed: "ZC08_20200607 Video 2 6_7_2020 11_23_33 AM 1.mp4" to "ZC08_20200607_Video_2_6_7_2020_11_23_33_AM_1.mp4"
# Renamed: "ZC09_20200628 Video 2 6_28_2020 10_54_38 AM 1.mp4" to "ZC09_20200628_Video_2_6_28_2020_10_54_38_AM_1.mp4"
# Renamed: "ZC10_20200628 Video 2 6_28_2020 11_12_52 AM 1.mp4" to "ZC10_20200628_Video_2_6_28_2020_11_12_52_AM_1.mp4"
# Renamed: "ZC11_20200712 Video 2 7_12_2020 11_10_00 AM 1.mp4" to "ZC11_20200712_Video_2_7_12_2020_11_10_00_AM_1.mp4"
# Renamed: "ZC12_20200712 Video 2 7_12_2020 11_28_37 AM 1.mp4" to "ZC12_20200712_Video_2_7_12_2020_11_28_37_AM_1.mp4"
# Renamed: "ZC13_20200809 Video 1 8_9_2020 11_07_42 AM 1.mp4" to "ZC13_20200809_Video_1_8_9_2020_11_07_42_AM_1.mp4"
# Renamed: "ZC14_20200809 Video 1 8_9_2020 11_26_03 AM 1.mp4" to "ZC14_20200809_Video_1_8_9_2020_11_26_03_AM_1.mp4"
# Renamed: "ZC15_20200816 Video 1 8_16_2020 11_06_52 AM 1.mp4" to "ZC15_20200816_Video_1_8_16_2020_11_06_52_AM_1.mp4"
# Renamed: "ZC17_20200913 Video 1 9_13_2020 11_14_56 AM 1.mp4" to "ZC17_20200913_Video_1_9_13_2020_11_14_56_AM_1.mp4"
# Renamed: "ZC18_20200913 Video 1 9_13_2020 11_50_24 AM 1.mp4" to "ZC18_20200913_Video_1_9_13_2020_11_50_24_AM_1.mp4"
# Renamed: "ZC19_20200920 Video 1 9_20_2020 11_21_14 AM 1.mp4" to "ZC19_20200920_Video_1_9_20_2020_11_21_14_AM_1.mp4"
# Renamed: "ZC20_20200920 Video 1 9_20_2020 11_47_42 AM 1.mp4" to "ZC20_20200920_Video_1_9_20_2020_11_47_42_AM_1.mp4"
# Renamed: "ZC21_20201018 Video 1 10_18_2020 11_09_20 AM 1.mp4" to "ZC21_20201018_Video_1_10_18_2020_11_09_20_AM_1.mp4"
# Renamed: "ZC22_20201018 Video 1 10_18_2020 11_41_07 AM 1.mp4" to "ZC22_20201018_Video_1_10_18_2020_11_41_07_AM_1.mp4"

# %%'
# %%' un-warp

# un-warp commands
    # || the fish-eye distortion
    # as it needs user input ( defining the edges of a curved side ), this can not be done fully automated !!

# Define the input directory
# uw : un-warp
input_dir = r'D:\video\pod_7'
output_dir = os.path.join(input_dir, 'uw')

# Ensure the output directory exists
    # if it doesn't exist, create one.
os.makedirs(output_dir, exist_ok=True)

# Iterate over files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.mp4'):  # Check if the file is an .mp4 video
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename.replace('.mp4', '_uw.mp4'))
        command = f'python undistort.py {input_path} {output_path} --balance 0.3'
        print(command)


# %%'  retrain_2 commands _ unwarp

# python undistort.py D:\video\retraining_2\P067_ZC61_OF2ReTr_Video_1_28_06_2023_11_01_15_1.mp4 D:\video\retraining_2\uw\P067_ZC61_OF2ReTr_Video_1_28_06_2023_11_01_15_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\P067_ZC62_OF2ReTr_Video_1_04_07_2023_10_52_25_1.mp4 D:\video\retraining_2\uw\P067_ZC62_OF2ReTr_Video_1_04_07_2023_10_52_25_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\P067_ZC63_OF2ReTr_Video_1_23_07_2023_10_57_39_1.mp4 D:\video\retraining_2\uw\P067_ZC63_OF2ReTr_Video_1_23_07_2023_10_57_39_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\P067_ZC64_OF2ReTr_Video_1_30_07_2023_11_01_35_1.mp4 D:\video\retraining_2\uw\P067_ZC64_OF2ReTr_Video_1_30_07_2023_11_01_35_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\P067_ZC65_OF2ReTr_Video_1_06_08_2023_11_03_57_1.mp4 D:\video\retraining_2\uw\P067_ZC65_OF2ReTr_Video_1_06_08_2023_11_03_57_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\P067_ZC66_OF2ReTr_Video_1_03_09_2023_10_56_43_1.mp4 D:\video\retraining_2\uw\P067_ZC66_OF2ReTr_Video_1_03_09_2023_10_56_43_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\P067_ZC67_OF2ReTr_Video_1_11_09_2023_10_44_13_1.mp4 D:\video\retraining_2\uw\P067_ZC67_OF2ReTr_Video_1_11_09_2023_10_44_13_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\P067_ZC68_OF2ReTr_Video_1_08_10_2023_10_48_19_1.mp4 D:\video\retraining_2\uw\P067_ZC68_OF2ReTr_Video_1_08_10_2023_10_48_19_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC04_20200216_Video_2_2_16_2020_11_03_19_AM_1.mp4 D:\video\retraining_2\uw\ZC04_20200216_Video_2_2_16_2020_11_03_19_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC05_20200309_Video_2_3_9_2020_11_10_13_AM_1.mp4 D:\video\retraining_2\uw\ZC05_20200309_Video_2_3_9_2020_11_10_13_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC06_20200309_Video_2_3_9_2020_11_34_04_AM_1.mp4 D:\video\retraining_2\uw\ZC06_20200309_Video_2_3_9_2020_11_34_04_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC07_20200607_Video_2_6_7_2020_10_59_59_AM_1.mp4 D:\video\retraining_2\uw\ZC07_20200607_Video_2_6_7_2020_10_59_59_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC08_20200607_Video_2_6_7_2020_11_23_33_AM_1.mp4 D:\video\retraining_2\uw\ZC08_20200607_Video_2_6_7_2020_11_23_33_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC09_20200628_Video_2_6_28_2020_10_54_38_AM_1.mp4 D:\video\retraining_2\uw\ZC09_20200628_Video_2_6_28_2020_10_54_38_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC10_20200628_Video_2_6_28_2020_11_12_52_AM_1.mp4 D:\video\retraining_2\uw\ZC10_20200628_Video_2_6_28_2020_11_12_52_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC11_20200712_Video_2_7_12_2020_11_10_00_AM_1.mp4 D:\video\retraining_2\uw\ZC11_20200712_Video_2_7_12_2020_11_10_00_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC12_20200712_Video_2_7_12_2020_11_28_37_AM_1.mp4 D:\video\retraining_2\uw\ZC12_20200712_Video_2_7_12_2020_11_28_37_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC13_20200809_Video_1_8_9_2020_11_07_42_AM_1.mp4 D:\video\retraining_2\uw\ZC13_20200809_Video_1_8_9_2020_11_07_42_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC14_20200809_Video_1_8_9_2020_11_26_03_AM_1.mp4 D:\video\retraining_2\uw\ZC14_20200809_Video_1_8_9_2020_11_26_03_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC15_20200816_Video_1_8_16_2020_11_06_52_AM_1.mp4 D:\video\retraining_2\uw\ZC15_20200816_Video_1_8_16_2020_11_06_52_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC17_20200913_Video_1_9_13_2020_11_14_56_AM_1.mp4 D:\video\retraining_2\uw\ZC17_20200913_Video_1_9_13_2020_11_14_56_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC18_20200913_Video_1_9_13_2020_11_50_24_AM_1.mp4 D:\video\retraining_2\uw\ZC18_20200913_Video_1_9_13_2020_11_50_24_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC19_20200920_Video_1_9_20_2020_11_21_14_AM_1.mp4 D:\video\retraining_2\uw\ZC19_20200920_Video_1_9_20_2020_11_21_14_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC20_20200920_Video_1_9_20_2020_11_47_42_AM_1.mp4 D:\video\retraining_2\uw\ZC20_20200920_Video_1_9_20_2020_11_47_42_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC21_20201018_Video_1_10_18_2020_11_09_20_AM_1.mp4 D:\video\retraining_2\uw\ZC21_20201018_Video_1_10_18_2020_11_09_20_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\retraining_2\ZC22_20201018_Video_1_10_18_2020_11_41_07_AM_1.mp4 D:\video\retraining_2\uw\ZC22_20201018_Video_1_10_18_2020_11_41_07_AM_1_uw.mp4 --balance 0.3

# %%' pod_1 commands _ unwarp

# python undistort.py D:\video\pod_1\P067_ZC60_POD1_Video_1_06_06_2023_11_22_38_1.mp4 D:\video\pod_1\uw\P067_ZC60_POD1_Video_1_06_06_2023_11_22_38_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\P067_ZC61_POD1_Video_1_30_06_2023_11_00_49_1.mp4 D:\video\pod_1\uw\P067_ZC61_POD1_Video_1_30_06_2023_11_00_49_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\P067_ZC62_POD1_Video_1_06_07_2023_11_10_52_1.mp4 D:\video\pod_1\uw\P067_ZC62_POD1_Video_1_06_07_2023_11_10_52_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\P067_ZC63_POD1_Video_1_25_07_2023_11_01_31_1.mp4 D:\video\pod_1\uw\P067_ZC63_POD1_Video_1_25_07_2023_11_01_31_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\P067_ZC65_POD1_Video_1_08_08_2023_10_55_42_1.mp4 D:\video\pod_1\uw\P067_ZC65_POD1_Video_1_08_08_2023_10_55_42_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\P067_ZC65_POD1_Video_1_08_08_2023_14_03_53_1.mp4 D:\video\pod_1\uw\P067_ZC65_POD1_Video_1_08_08_2023_14_03_53_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\P067_ZC66_POD1_Video_1_05_09_2023_10_58_33_1.mp4 D:\video\pod_1\uw\P067_ZC66_POD1_Video_1_05_09_2023_10_58_33_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\P067_ZC67_POD1_Video_1_13_09_2023_11_10_55_1.mp4 D:\video\pod_1\uw\P067_ZC67_POD1_Video_1_13_09_2023_11_10_55_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\P067_ZC68_POD1_Video_1_10_10_2023_11_03_52_1.mp4 D:\video\pod_1\uw\P067_ZC68_POD1_Video_1_10_10_2023_11_03_52_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\P067_ZC69_POD1_Video_1_24_10_2023_11_00_02_1.mp4 D:\video\pod_1\uw\P067_ZC69_POD1_Video_1_24_10_2023_11_00_02_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC04_20200219_Video_2_2_19_2020_11_11_14_AM_1.mp4 D:\video\pod_1\uw\ZC04_20200219_Video_2_2_19_2020_11_11_14_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC05_20200312_Video_2_3_12_2020_11_03_19_AM_1.mp4 D:\video\pod_1\uw\ZC05_20200312_Video_2_3_12_2020_11_03_19_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC06_20200312_Video_2_3_12_2020_11_18_50_AM_1.mp4 D:\video\pod_1\uw\ZC06_20200312_Video_2_3_12_2020_11_18_50_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC07_20200610_Video_2_6_10_2020_11_00_34_AM_1.mp4 D:\video\pod_1\uw\ZC07_20200610_Video_2_6_10_2020_11_00_34_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC08_20200610_Video_2_6_10_2020_11_37_19_AM_1.mp4 D:\video\pod_1\uw\ZC08_20200610_Video_2_6_10_2020_11_37_19_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC09_20200701_Video_2_7_1_2020_10_58_56_AM_1.mp4 D:\video\pod_1\uw\ZC09_20200701_Video_2_7_1_2020_10_58_56_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC10_20200701_Video_2_7_1_2020_11_15_25_AM_1.mp4 D:\video\pod_1\uw\ZC10_20200701_Video_2_7_1_2020_11_15_25_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC11_20200715_Video_2_7_15_2020_11_21_59_AM_1.mp4 D:\video\pod_1\uw\ZC11_20200715_Video_2_7_15_2020_11_21_59_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC14_20200812_Video_1_8_12_2020_10_57_48_AM_1.mp4 D:\video\pod_1\uw\ZC14_20200812_Video_1_8_12_2020_10_57_48_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC15_20200819_Video_1_8_19_2020_11_16_30_AM_1.mp4 D:\video\pod_1\uw\ZC15_20200819_Video_1_8_19_2020_11_16_30_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC17_20200916_Video_1_9_16_2020_11_07_12_AM_1.mp4 D:\video\pod_1\uw\ZC17_20200916_Video_1_9_16_2020_11_07_12_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC19_20200923_Video_1_9_23_2020_10_58_06_AM_1.mp4 D:\video\pod_1\uw\ZC19_20200923_Video_1_9_23_2020_10_58_06_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC20_20200923_Video_1_9_23_2020_11_14_05_AM_1.mp4 D:\video\pod_1\uw\ZC20_20200923_Video_1_9_23_2020_11_14_05_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC21_20201021_Video_1_10_21_2020_10_39_13_AM_1.mp4 D:\video\pod_1\uw\ZC21_20201021_Video_1_10_21_2020_10_39_13_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_1\ZC22_20201021_Video_1_10_21_2020_10_53_59_AM_1.mp4 D:\video\pod_1\uw\ZC22_20201021_Video_1_10_21_2020_10_53_59_AM_1_uw.mp4 --balance 0.3

# %% pod_3 commands _ unwarp

# python undistort.py D:\video\pod_3\P067_ZC60_POD3_Video_1_08_06_2023_08_20_56_1.mp4 D:\video\pod_3\uw\P067_ZC60_POD3_Video_1_08_06_2023_08_20_56_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\P067_ZC61_POD3_Video_1_02_07_2023_10_59_34_1.mp4 D:\video\pod_3\uw\P067_ZC61_POD3_Video_1_02_07_2023_10_59_34_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\P067_ZC62_POD2_Extra_Neu_Video_1_07_07_2023_10_16_44_1.mp4 D:\video\pod_3\uw\P067_ZC62_POD2_Extra_Neu_Video_1_07_07_2023_10_16_44_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\P067_ZC63_POD3_Video_1_27_07_2023_10_56_47_1.mp4 D:\video\pod_3\uw\P067_ZC63_POD3_Video_1_27_07_2023_10_56_47_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\P067_ZC65_POD3_Video_1_10_08_2023_10_59_05_1.mp4 D:\video\pod_3\uw\P067_ZC65_POD3_Video_1_10_08_2023_10_59_05_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\P067_ZC66_POD3_Video_1_07_09_2023_11_00_35_1.mp4 D:\video\pod_3\uw\P067_ZC66_POD3_Video_1_07_09_2023_11_00_35_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\P067_ZC67_POD3_Video_1_15_09_2023_11_05_17_1.mp4 D:\video\pod_3\uw\P067_ZC67_POD3_Video_1_15_09_2023_11_05_17_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\P067_ZC68_POD3_Video_1_12_10_2023_10_56_51_1.mp4 D:\video\pod_3\uw\P067_ZC68_POD3_Video_1_12_10_2023_10_56_51_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\P067_ZC69_POD3_Video_1_26_10_2023_11_00_10_1.mp4 D:\video\pod_3\uw\P067_ZC69_POD3_Video_1_26_10_2023_11_00_10_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC04_20200221_Video_2_2_21_2020_11_10_04_AM_1.mp4 D:\video\pod_3\uw\ZC04_20200221_Video_2_2_21_2020_11_10_04_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC05_20200314_Video_2_3_14_2020_11_02_36_AM_1.mp4 D:\video\pod_3\uw\ZC05_20200314_Video_2_3_14_2020_11_02_36_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC06_20200314_Video_2_3_14_2020_11_29_26_AM_1.mp4 D:\video\pod_3\uw\ZC06_20200314_Video_2_3_14_2020_11_29_26_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC07_20200610_Video_2_6_12_2020_10_55_38_AM_1.mp4 D:\video\pod_3\uw\ZC07_20200610_Video_2_6_12_2020_10_55_38_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC08_20200610_Video_2_6_12_2020_11_19_38_AM_1.mp4 D:\video\pod_3\uw\ZC08_20200610_Video_2_6_12_2020_11_19_38_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC09_20200703_Video_2_7_3_2020_11_12_35_AM_1.mp4 D:\video\pod_3\uw\ZC09_20200703_Video_2_7_3_2020_11_12_35_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC10_20200703_Video_2_7_3_2020_11_38_25_AM_1.mp4 D:\video\pod_3\uw\ZC10_20200703_Video_2_7_3_2020_11_38_25_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC11_20200717_Video_2_7_17_2020_11_28_43_AM_1.mp4 D:\video\pod_3\uw\ZC11_20200717_Video_2_7_17_2020_11_28_43_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC14_20200814_Video_1_8_14_2020_11_04_56_AM_1.mp4 D:\video\pod_3\uw\ZC14_20200814_Video_1_8_14_2020_11_04_56_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC15_20200821_Video_1_8_21_2020_11_06_40_AM_1.mp4 D:\video\pod_3\uw\ZC15_20200821_Video_1_8_21_2020_11_06_40_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC17_20200918_Video_1_9_18_2020_11_08_55_AM_1.mp4 D:\video\pod_3\uw\ZC17_20200918_Video_1_9_18_2020_11_08_55_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC19_20200925_Video_1_9_25_2020_10_46_41_AM_1.mp4 D:\video\pod_3\uw\ZC19_20200925_Video_1_9_25_2020_10_46_41_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC20_20200925_Video_1_9_25_2020_11_07_24_AM_1.mp4 D:\video\pod_3\uw\ZC20_20200925_Video_1_9_25_2020_11_07_24_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC21_20201023_Video_1_10_23_2020_11_08_54_AM_1.mp4 D:\video\pod_3\uw\ZC21_20201023_Video_1_10_23_2020_11_08_54_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_3\ZC22_20201023_Video_1_10_23_2020_11_32_43_AM_1.mp4 D:\video\pod_3\uw\ZC22_20201023_Video_1_10_23_2020_11_32_43_AM_1_uw.mp4 --balance 0.3

# %% pod_4 commands _ unwarp

# python undistort.py D:\video\pod_4\P067_ZC61_POD4_Video_1_03_07_2023_11_01_51_1.mp4 D:\video\pod_4\uw\P067_ZC61_POD4_Video_1_03_07_2023_11_01_51_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\P067_ZC63_POD4_Video_1_28_07_2023_11_13_43_1.mp4 D:\video\pod_4\uw\P067_ZC63_POD4_Video_1_28_07_2023_11_13_43_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\P067_ZC66_POD4_Video_1_08_09_2023_10_54_46_1.mp4 D:\video\pod_4\uw\P067_ZC66_POD4_Video_1_08_09_2023_10_54_46_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\P067_ZC67_POD4_Video_1_16_09_2023_10_57_44_1.mp4 D:\video\pod_4\uw\P067_ZC67_POD4_Video_1_16_09_2023_10_57_44_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\P067_ZC68_POD4_Video_1_13_10_2023_10_59_09_1.mp4 D:\video\pod_4\uw\P067_ZC68_POD4_Video_1_13_10_2023_10_59_09_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC04_20200222_Video_2_2_22_2020_11_11_38_AM_1.mp4 D:\video\pod_4\uw\ZC04_20200222_Video_2_2_22_2020_11_11_38_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC05_20200315_Video_2_3_15_2020_11_12_22_AM_1.mp4 D:\video\pod_4\uw\ZC05_20200315_Video_2_3_15_2020_11_12_22_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC06_20200315_Video_2_3_15_2020_11_37_59_AM_1.mp4 D:\video\pod_4\uw\ZC06_20200315_Video_2_3_15_2020_11_37_59_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC07_20200613_Video_2_6_13_2020_1_03_18_PM_1.mp4 D:\video\pod_4\uw\ZC07_20200613_Video_2_6_13_2020_1_03_18_PM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC08_20200613_Video_2_6_13_2020_11_03_21_AM_1.mp4 D:\video\pod_4\uw\ZC08_20200613_Video_2_6_13_2020_11_03_21_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC09_20200704_Video_2_7_4_2020_11_25_24_AM_1.mp4 D:\video\pod_4\uw\ZC09_20200704_Video_2_7_4_2020_11_25_24_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC10_20200704_Video_2_7_4_2020_11_45_07_AM_1.mp4 D:\video\pod_4\uw\ZC10_20200704_Video_2_7_4_2020_11_45_07_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC11_20200718_Video_2_7_18_2020_11_00_59_AM_1.mp4 D:\video\pod_4\uw\ZC11_20200718_Video_2_7_18_2020_11_00_59_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC14_20200815_Video_1_8_15_2020_11_10_17_AM_1.mp4 D:\video\pod_4\uw\ZC14_20200815_Video_1_8_15_2020_11_10_17_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC15_20200822_Video_1_8_22_2020_11_06_53_AM_1.mp4 D:\video\pod_4\uw\ZC15_20200822_Video_1_8_22_2020_11_06_53_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC19_20200926_Video_1_9_26_2020_11_36_18_AM_1.mp4 D:\video\pod_4\uw\ZC19_20200926_Video_1_9_26_2020_11_36_18_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC20_20200926_Video_1_9_26_2020_11_11_58_AM_1.mp4 D:\video\pod_4\uw\ZC20_20200926_Video_1_9_26_2020_11_11_58_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC21_20201024_Video_1_10_24_2020_11_05_59_AM_1.mp4 D:\video\pod_4\uw\ZC21_20201024_Video_1_10_24_2020_11_05_59_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_4\ZC22_20201024_Video_1_10_24_2020_12_54_30_PM_1.mp4 D:\video\pod_4\uw\ZC22_20201024_Video_1_10_24_2020_12_54_30_PM_1_uw.mp4 --balance 0.3

# %% pod_7 commands _ unwarp

# python undistort.py D:\video\pod_7\P067_ZC61_POD7_Video_1_06_07_2023_10_52_22_1.mp4 D:\video\pod_7\uw\P067_ZC61_POD7_Video_1_06_07_2023_10_52_22_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\P067_ZC63_POD7_Video_1_31_07_2023_11_05_54_1.mp4 D:\video\pod_7\uw\P067_ZC63_POD7_Video_1_31_07_2023_11_05_54_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\P067_ZC66_POD7_Video_1_11_09_2023_11_27_00_1.mp4 D:\video\pod_7\uw\P067_ZC66_POD7_Video_1_11_09_2023_11_27_00_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\P067_ZC67_POD7_Video_1_19_09_2023_10_57_59_1.mp4 D:\video\pod_7\uw\P067_ZC67_POD7_Video_1_19_09_2023_10_57_59_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\P067_ZC68_POD7_Video_1_16_10_2023_10_58_24_1.mp4 D:\video\pod_7\uw\P067_ZC68_POD7_Video_1_16_10_2023_10_58_24_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\ZC05_20200318_Video_2_3_18_2020_11_03_18_AM_1.mp4 D:\video\pod_7\uw\ZC05_20200318_Video_2_3_18_2020_11_03_18_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\ZC07_20200616_Video_2_6_16_2020_10_59_45_AM_1.mp4 D:\video\pod_7\uw\ZC07_20200616_Video_2_6_16_2020_10_59_45_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\ZC08_20200616_Video_2_6_16_2020_11_27_16_AM_1.mp4 D:\video\pod_7\uw\ZC08_20200616_Video_2_6_16_2020_11_27_16_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\ZC09_20200707_Video_2_7_7_2020_11_31_34_AM_1.mp4 D:\video\pod_7\uw\ZC09_20200707_Video_2_7_7_2020_11_31_34_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\ZC10_20200707_Video_2_7_7_2020_11_12_14_AM_1.mp4 D:\video\pod_7\uw\ZC10_20200707_Video_2_7_7_2020_11_12_14_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\ZC11_20200721_Video_2_7_21_2020_11_26_22_AM_1.mp4 D:\video\pod_7\uw\ZC11_20200721_Video_2_7_21_2020_11_26_22_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\ZC14_20200818_Video_1_8_18_2020_11_06_07_AM_1.mp4 D:\video\pod_7\uw\ZC14_20200818_Video_1_8_18_2020_11_06_07_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\ZC15_20200825_Video_1_8_25_2020_11_02_39_AM_1.mp4 D:\video\pod_7\uw\ZC15_20200825_Video_1_8_25_2020_11_02_39_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\ZC19_20200929_Video_1_9_29_2020_11_09_52_AM_1.mp4 D:\video\pod_7\uw\ZC19_20200929_Video_1_9_29_2020_11_09_52_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\ZC20_20200929_Video_1_9_29_2020_11_33_32_AM_1.mp4 D:\video\pod_7\uw\ZC20_20200929_Video_1_9_29_2020_11_33_32_AM_1_uw.mp4 --balance 0.3
# python undistort.py D:\video\pod_7\ZC21_20201027_Video_1_10_27_2020_11_06_06_AM_1.mp4 D:\video\pod_7\uw\ZC21_20201027_Video_1_10_27_2020_11_06_06_AM_1_uw.mp4 --balance 0.3

# python undistort.py D:\video\pod_7\ZC22_20201027_Video_1_10_27_2020_11_26_56_AM_1.mp4 D:\video\pod_7\uw\ZC22_20201027_Video_1_10_27_2020_11_26_56_AM_1_uw.mp4 --balance 0.3

# %%'

# explore

output_dir
    # Out[28]: 'D:\\video\\retraining_2\\uw'

# %% histogram_equalization

# histogram_equalization command
    # this generates commands for each single file !
    # you should then copy-paste them manually into the terminal & wait for them to be finished ! => then the next file !

input_dir = r'D:\video\retraining_2\uw'
output_dir = r'D:\video\retraining_2\heq'

# Ensure the output directory exists
# os.makedirs(output_dir, exist_ok=True)

# Iterate over files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.mp4'):  # Check if the file is an .mp4 video
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename.replace('.mp4', '_heq.mp4'))
        command = f'python histogram_equalization.py  {input_path} {output_path}'
        print(command)


# %%'

# python histogram_equalization.py  D:\video\retraining_2\uw\P067_ZC63_OF2ReTr_Video_1_23_07_2023_10_57_39_1_uw.mp4 D:\video\retraining_2\heq\P067_ZC63_OF2ReTr_Video_1_23_07_2023_10_57_39_1_uw_heq.mp4
# python histogram_equalization.py  D:\video\retraining_2\uw\P067_ZC64_OF2ReTr_Video_1_30_07_2023_11_01_35_1_uw.mp4 D:\video\retraining_2\heq\P067_ZC64_OF2ReTr_Video_1_30_07_2023_11_01_35_1_uw_heq.mp4
# python histogram_equalization.py  D:\video\retraining_2\uw\P067_ZC65_OF2ReTr_Video_1_06_08_2023_11_03_57_1_uw.mp4 D:\video\retraining_2\heq\P067_ZC65_OF2ReTr_Video_1_06_08_2023_11_03_57_1_uw_heq.mp4
# python histogram_equalization.py  D:\video\retraining_2\uw\P067_ZC66_OF2ReTr_Video_1_03_09_2023_10_56_43_1_uw.mp4 D:\video\retraining_2\heq\P067_ZC66_OF2ReTr_Video_1_03_09_2023_10_56_43_1_uw_heq.mp4
# python histogram_equalization.py  D:\video\retraining_2\uw\P067_ZC67_OF2ReTr_Video_1_11_09_2023_10_44_13_1_uw.mp4 D:\video\retraining_2\heq\P067_ZC67_OF2ReTr_Video_1_11_09_2023_10_44_13_1_uw_heq.mp4
# python histogram_equalization.py  D:\video\retraining_2\uw\P067_ZC68_OF2ReTr_Video_1_08_10_2023_10_48_19_1_uw.mp4 D:\video\retraining_2\heq\P067_ZC68_OF2ReTr_Video_1_08_10_2023_10_48_19_1_uw_heq.mp4

# for the rest of the files ( starting with zc ... ) histogram equalization is not needed.

# %% histogram equalization : multiple files

# this automates running the sub-process for multiple files.
    # since unlike the unwarping, there is no user input !
        # it can run un-supervised !
# U:\VISION\track\pre-process \ filename .docx
    # conversation with AI

import subprocess
from pathlib import Path

# %%'

'''
                The glob() method on a Path object returns an iterator over all files in that directory matching the given pattern. 
                    By using f'*{ext}' (for example *.mp4), you tell Python to include every file whose name ends with that extension.
                    Each item yielded by glob() is a Path object, so you can treat it like a path rather than a plain string.
                
                When you call subprocess.run(...) with check=True :
                    Python will automatically raise a CalledProcessError if the external program exits with a non-zero status.
'''

# === Configure paths and extension ===
input_dir   = Path(r'D:\video\pod_7\uw\low_light')
output_dir  = Path(r'D:\video\pod_7\uw\equalized')
script_path = Path(r'U:\VISION\track\pre-process\histogram_equalization.py')
ext         = '.mp4'


# === Prepare output directory ===
    #  create a directory if it does not exist.
output_dir.mkdir(parents=True, exist_ok=True)   


# === Loop through videos ===
for video_path in input_dir.glob(f'*{ext}'):    # fetch any .mp4 file !
    # build new filename: stem + "_eq" + suffix
    new_name = f"{video_path.stem}_eq{video_path.suffix}"   # add _eq ( histogram equalized ) suffix to the new file.
    out_path = output_dir / new_name
    print(f'Processing: {video_path.name}')
    subprocess.run([
                    'python',
                    str(script_path),
                    str(video_path),
                    str(out_path)
                    ]
    , check=True
    )

print('Done!')

# %%'

# Processing: P067_ZC60_POD1_Video_1_06_06_2023_11_22_38_1_uw.mp4
# Processing: P067_ZC61_POD1_Video_1_30_06_2023_11_00_49_1_uw.mp4
# Processing: P067_ZC62_POD1_Video_1_06_07_2023_11_10_52_1_uw.mp4
# Processing: P067_ZC63_POD1_Video_1_25_07_2023_11_01_31_1_uw.mp4
# Processing: P067_ZC65_POD1_Video_1_08_08_2023_10_55_42_1_uw.mp4
# Processing: P067_ZC66_POD1_Video_1_05_09_2023_10_58_33_1_uw.mp4
# Processing: P067_ZC67_POD1_Video_1_13_09_2023_11_10_55_1_uw.mp4
# Processing: P067_ZC68_POD1_Video_1_10_10_2023_11_03_52_1_uw.mp4
# Processing: P067_ZC69_POD1_Video_1_24_10_2023_11_00_02_1_uw.mp4
# Done!

# %% create a folder for each video file => move the file to that folder !

from pathlib import Path
import shutil

# %%'

# 1) Configure your input directory
input_dir = Path(r"D:\video\pod_7\uw\corrected")

# 2) Loop over every .mp4 file
    # the directory in-which the videos exist
for video_path in input_dir.glob("*.mp4"):
    # video_path.stem is the filename without the .mp4, e.g.
    # "ZC06_20200312_Video_2_3_12_2020_11_18_50_AM_1_uw"
    stem = video_path.stem
    
    # 3) Remove the trailing "_uw" to get the folder name
    folder_name = stem.removesuffix("_uw")
    
    # 4) Define and create the new folder
    folder_path = input_dir / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)
    
    # 5) Move the video into its folder
    destination = folder_path / video_path.name
    shutil.move(str(video_path), str(destination))
    
    print(f"Moved {video_path.name} → {folder_path.name}/")

print("All videos have been organized into individual folders.")

# %%  _uw_eq removal

import re
from pathlib import Path
import shutil

# to remove also _eq from the name of the file & set it as a folder name.

# 1) Configure your input directory
input_dir = Path(r"D:\video\pod_3\uw\corrected")

# this regex will remove any of these at the end: _uw_eq, _uw or _eq
SUFFIX_RE = re.compile(r'_(?:uw_eq|uw|eq)$')

for video_path in input_dir.glob("*.mp4"):
    
    stem = video_path.stem
    folder_name = SUFFIX_RE.sub('', stem)
    
    folder_path = input_dir / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)
    
    destination = folder_path / video_path.name
    shutil.move(str(video_path), str(destination))
    print(f"Moved {video_path.name} → {folder_path.name}/")

print("All videos have been organized into individual folders.")

# %% move file to folder

# moving fies to a folder with the same name as the file ( without removing any suffixes from the file name ).

# 1) Configure your input directory
input_dir = Path(r"D:\video\pod_3\uw\corrected")

# 2) Loop over every .mp4 file
for video_path in input_dir.glob("*.mp4"):
    # video_path.stem includes all suffixes (e.g. "name_uw_eq")
    folder_name = video_path.stem

    # 3) Define and create the new folder
    folder_path = input_dir / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)

    # 4) Move the video into its folder
    destination = folder_path / video_path.name
    shutil.move(str(video_path), str(destination))

    print(f"Moved {video_path.name} → {folder_path.name}/")

print("All videos have been organized into individual folders.")


# %%'

# Moved ZC04_20200219_Video_2_2_19_2020_11_11_14_AM_1_uw.mp4 → ZC04_20200219_Video_2_2_19_2020_11_11_14_AM_1/
# Moved ZC05_20200312_Video_2_3_12_2020_11_03_19_AM_1_uw.mp4 → ZC05_20200312_Video_2_3_12_2020_11_03_19_AM_1/
# Moved ZC06_20200312_Video_2_3_12_2020_11_18_50_AM_1_uw.mp4 → ZC06_20200312_Video_2_3_12_2020_11_18_50_AM_1/
# Moved ZC07_20200610_Video_2_6_10_2020_11_00_34_AM_1_uw.mp4 → ZC07_20200610_Video_2_6_10_2020_11_00_34_AM_1/
# Moved ZC08_20200610_Video_2_6_10_2020_11_37_19_AM_1_uw.mp4 → ZC08_20200610_Video_2_6_10_2020_11_37_19_AM_1/
# Moved ZC09_20200701_Video_2_7_1_2020_10_58_56_AM_1_uw.mp4 → ZC09_20200701_Video_2_7_1_2020_10_58_56_AM_1/
# Moved ZC10_20200701_Video_2_7_1_2020_11_15_25_AM_1_uw.mp4 → ZC10_20200701_Video_2_7_1_2020_11_15_25_AM_1/
# Moved ZC11_20200715_Video_2_7_15_2020_11_21_59_AM_1_uw.mp4 → ZC11_20200715_Video_2_7_15_2020_11_21_59_AM_1/
# Moved ZC14_20200812_Video_1_8_12_2020_10_57_48_AM_1_uw.mp4 → ZC14_20200812_Video_1_8_12_2020_10_57_48_AM_1/
# Moved ZC15_20200819_Video_1_8_19_2020_11_16_30_AM_1_uw.mp4 → ZC15_20200819_Video_1_8_19_2020_11_16_30_AM_1/
# Moved ZC17_20200916_Video_1_9_16_2020_11_07_12_AM_1_uw.mp4 → ZC17_20200916_Video_1_9_16_2020_11_07_12_AM_1/
# Moved ZC19_20200923_Video_1_9_23_2020_10_58_06_AM_1_uw.mp4 → ZC19_20200923_Video_1_9_23_2020_10_58_06_AM_1/
# Moved ZC20_20200923_Video_1_9_23_2020_11_14_05_AM_1_uw.mp4 → ZC20_20200923_Video_1_9_23_2020_11_14_05_AM_1/
# Moved ZC21_20201021_Video_1_10_21_2020_10_39_13_AM_1_uw.mp4 → ZC21_20201021_Video_1_10_21_2020_10_39_13_AM_1/
# Moved ZC22_20201021_Video_1_10_21_2020_10_53_59_AM_1_uw.mp4 → ZC22_20201021_Video_1_10_21_2020_10_53_59_AM_1/
# All videos have been organized into individual folders.

# %% extract the 1st frame _ all videos

# this extracts the 1st frames from all videos in a directory.
# this was done to then calculate the pixel-meter length conversion.
    # this information is needed to calculate the total distance traveled.

import os
import subprocess

# %%'


'''
        questions :
            
            for dirpath , dirnames , filenames in ...
                dirnames : 
                    what is it ?
                    it was not used.
                    
                    
            subprocess.run(command, capture_output=True, text=True, check=True)
                what are the kwargs ?
                    capture_output=True, text=True, check=True

'''


# The function is now a generic tool that can work on ANY directory you give it.
def extract_first_frame_in_directory(target_dir):
    """
            Scans subdirectories of a given target folder for a video named 'Quality.mp4',
            extracts the first frame, and saves it as 'first_frame.png'.
    """
    if not os.path.isdir(target_dir):
        print(f"Error: Directory not found at '{target_dir}'")
        return

    print(f"Starting scan in root directory: {target_dir}\n")

    for dirpath , dirnames , filenames in os.walk(target_dir) :
        if "Quality.mp4" in filenames:
            video_path = os.path.join(dirpath, "Quality.mp4")
            output_path = os.path.join(dirpath, "first_frame.png")
            
            print(f"Found video: {video_path}")
            command = [
                        'ffmpeg',
                        '-i', video_path,       # Input file
                        '-vframes', '1',        # Extract only 1 video frame
                        '-y',                   # Overwrite output file if it exists, avoids script getting stuck
                        output_path             # Output file
            ]

            try:
                subprocess.run( command, capture_output=True, text=True, check=True )
                print(f"  -> Successfully extracted frame to: {output_path}")
            except Exception as e:
                print(f"  -> An error occurred: {e}")

    print("\nScan finished for directory:", target_dir)

# %%'


# --- Execution ---
# Now, you just need to call the function with the path you want to process.
# If you need to process another folder later, you just add another line.

directory_to_process_1 = r"U:\VISION\track\data\retrain_2"
extract_first_frame_in_directory(directory_to_process_1)

# Example: If you have another folder, you can run it again instantly:
# directory_to_process_2 = r"U:\VISION\track\data\new_batch"
# extract_first_frame_in_directory(directory_to_process_2)

# %%'

    # Starting scan in root directory: U:\VISION\track\data\retrain_2
    
    # Found video: U:\VISION\track\data\retrain_2\P067_ZC60_OF2ReTr_Video_1_04_06_2023_11_35_42_1\Quality.mp4
    #   -> Successfully extracted frame to: U:\VISION\track\data\retrain_2\P067_ZC60_OF2ReTr_Video_1_04_06_2023_11_35_42_1\first_frame.png
    # Found video: U:\VISION\track\data\retrain_2\P067_ZC61_OF2ReTr_Video_1_28_06_2023_11_01_15_1\Quality.mp4
    #   -> Successfully extracted frame to: U:\VISION\track\data\retrain_2\P067_ZC61_OF2ReTr_Video_1_28_06_2023_11_01_15_1\first_frame.png
    # Found video: U:\VISION\track\data\retrain_2\P067_ZC62_OF2ReTr_Video_1_04_07_2023_10_52_25_1\Quality.mp4
    # ...

# %%'

# this extracts the first frame from all videos.
extract_first_frame_in_directory( r'U:\data\track_data' )

# %% organizing 1st frames' file structure ( parent folder pathes ).

# this was done in : C:\code\VISION\track\first_frame.py


# %%'
# %%' first frame from only one video

# if you want to extract the first frame from only one video !

from pathlib import Path
import subprocess

# %%'

# this must be done, otherewise, single '\' intsead of  '\\' would make trouble !
video_path = Path(r'U:\VISION\track\data\retrain_2\P067_ZC60_OF2ReTr_Video_1_04_06_2023_11_35_42_1\P067_ZC60_OF2ReTr_Video_1_04_06_2023_11_35_42_1.mp4')
output_path = Path(r'U:\VISION\track\data\retrain_2\P067_ZC60_OF2ReTr_Video_1_04_06_2023_11_35_42_1\first_frame_original.png')

command = [
            'ffmpeg',
            '-i', str(video_path),
            '-vframes', '1',
            '-y',
            str(output_path)
]

subprocess.run(command, capture_output=True, text=True, check=True)

# %%'

video_path
    # Out[43]: WindowsPath('U:/VISION/track/data/retrain_2/P067_ZC60_OF2ReTr_Video_1_04_06_2023_11_35_42_1/P067_ZC60_OF2ReTr_Video_1_04_06_2023_11_35_42_1.mp4')

# the output text is saved in : track .docx : under : Subprocess complete

# %%' extract & copy "center_points.csv" 
# extract & copy "center_points.csv" to a destination directory while \
        # preserving ( recreating ) that file's parent folder structure within the destination folder.
# F:\OneDrive - Uniklinik RWTH Aachen\IT\system__python \ AI__system__python .docx

import shutil
from pathlib import Path

# %%'

# --- Configuration ---
# Please set your source and destination folders here.
# Using raw strings (r"...") is a good practice for Windows paths.
source_folder = Path(r"U:\data\track_data")
destination_folder = Path(r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\extract")
file_to_copy = "center_points.csv"  # this is the file names & actually a kind of pattern to be searched ( .rglob ) later below.

# --- Script Logic ---
print(f"🚀 Starting the copy process...")
print(f"Source: {source_folder}")
print(f"Destination: {destination_folder}")
print("-" * 30)

# Check if the source folder exists
if not source_folder.is_dir():
    print(f"❌ Error: Source folder not found at '{source_folder}'")
else:
    # Use rglob() to recursively find all files with the specified name
    # The '**' part means it will search in the current directory and all subdirectories.
    # the list contains the full path of each file, including the file's name itself ( center_points.csv ).
    files_found = list(source_folder.rglob(f"**/{file_to_copy}"))
    
    if not files_found:
        print(f"🤷 No files named '{file_to_copy}' were found in the source directory.")
    else:
        print(f"✅ Found {len(files_found)} file(s) to copy.")
        
        for source_file_path in files_found:
            # Determine the file's path relative to the source folder's root
            # Example: U:\data\track_data\folder_1\file.csv -> folder_1\file.csv
            relative_path = source_file_path.relative_to(source_folder)
            
            # Create the full destination path
            # Example: F:\...\extract + folder_1\file.csv
            destination_file_path = destination_folder / relative_path
            
            # Create the necessary parent directories in the destination
            # The .parent attribute gets the directory containing the file
            # exist_ok=True prevents an error if the directory already exists
            destination_file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy the file, preserving metadata (like timestamps)
            shutil.copy2(source_file_path, destination_file_path)
            
            print(f"  -> Copied: {destination_file_path}")
            
        print("-" * 30)
        print("🎉 All files copied successfully!")

# %%'
# explore

# ✅ Found 111 file(s) to copy.

source_file_path
    # Out[4]: WindowsPath('U:/data/track_data/pod_1/ZC22_20201021_Video_1_10_21_2020_10_53_59_AM_1/center_points.csv')

relative_path
    # Out[5]: WindowsPath('pod_1/ZC22_20201021_Video_1_10_21_2020_10_53_59_AM_1/center_points.csv')

destination_file_path
    # Out[6]: WindowsPath('F:/OneDrive - Uniklinik RWTH Aachen/VISION/track/extract/pod_1/ZC22_20201021_Video_1_10_21_2020_10_53_59_AM_1/center_points.csv')

# %%' copy the .csv files
# copy the .csv files to a new folder :
    # get rid of each file being in a separate folder.
    # change the name of the file to represent time-group ( retrain_2 , ... ) & animal label ( ZCnn ).
# # F:\OneDrive - Uniklinik RWTH Aachen\IT\system__python \ AI__system__python .docx

# %%'

import shutil
import re
from pathlib import Path

# %%'


# --- Configuration ---
# Source directory (populated by the first script)
source_folder = Path(r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\extract")

# Corrected final destination for the renamed and summarized files
destination_folder_2 = Path(r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\center_point")

file_to_find = "center_points.csv"

# --- Script Logic ---
print("🚀 Starting the rename and copy process...")
print(f"Source: {source_folder}")
print(f"Final Destination: {destination_folder_2}")
print("-" * 30)

# Check if the source folder exists
if not source_folder.is_dir():
    print(f"❌ Error: Source folder not found at '{source_folder}'")
else:
    # Recursively find all 'center_points.csv' files
    files_to_process = list(source_folder.rglob(f"**/{file_to_find}"))
    
    if not files_to_process:
        print(f"🤷 No files named '{file_to_find}' were found in the source directory.")
    else:
        print(f"✅ Found {len(files_to_process)} file(s) to process.")
        
        # Ensure the base destination directory exists
        destination_folder_2.mkdir(exist_ok=True)
        
        for source_file_path in files_to_process:
            try:
                # Get the names of the parent folders
                folder_2_name = source_file_path.parent.name
                folder_1_name = source_file_path.parent.parent.name
                
                # Use a regular expression to find the 'ZC##' pattern
                match = re.search(r'ZC\d{2}', folder_2_name)
                
                if match:
                    # The pattern was found, e.g., 'ZC04'
                    zc_code = match.group(0)
                    
                    # Construct the new filename, e.g., "pod_4_ZC04.csv"
                    new_filename = f"{folder_1_name}_{zc_code}.csv"
                    
                    # Construct the new destination folder path, e.g., ".../center_point/pod_4"
                    new_destination_folder = destination_folder_2 / folder_1_name
                    
                    # Create this folder if it doesn't exist
                    new_destination_folder.mkdir(parents=True, exist_ok=True)
                    
                    # Construct the full final path for the new file
                    final_file_path = new_destination_folder / new_filename
                    
                    # Copy the original file to the new location with the new name
                    # note : final_file_path : contains the file name & extension !
                        # this may not always be the case when copying files !
                    shutil.copy2(source_file_path, final_file_path)
                    
                    print(f"  -> Created: {final_file_path}")
                    
                else:
                    print(f"  -> ⚠️  Warning: Could not find 'ZC##' pattern in '{folder_2_name}'. Skipping file.")

            except IndexError:
                print(f"  -> ⚠️  Warning: File is not in a 'folder_1/folder_2' structure. Skipping {source_file_path}")

        print("-" * 30)
        print("🎉 All files processed successfully!")

# %%' rename 

# rename files, adding-up the figure number : example : Figure_4.svg  =>  Figure_5.svg
# F:\OneDrive - Uniklinik RWTH Aachen\IT\system__python \ AI__system__python .docx

# %%'

import os
import re
from pathlib import Path

# %%'

# --- Configuration ---
# PASTE YOUR FOLDER PATH HERE
folder_path = Path(r"V:\Labor (VT)\AG Tolba (VT)\P067 NTx Schwein\Results\plots_manuscript\2025-9-17__SEM")

# --- Script Logic ---
print(f"🔍 Scanning folder: {folder_path}\n")

# Regular expression to find files named "Figure_<number>.<extension>"
# It captures the number and the extension.
# a pattern : you can rename to 'pattern' !
regex = re.compile(r'^Figure_(\d+)\.(.+)$')

files_to_rename = []

# First, find and parse all matching files
for item in folder_path.iterdir():
    if item.is_file():
        match = regex.match(item.name)
        if match:
            number = int(match.group(1))
            extension = match.group(2)
            files_to_rename.append({
                "path": item,
                "number": number,
                "extension": extension
            })

# CRITICAL STEP: Sort the files by number in DESCENDING order
# This prevents renaming Figure_2.pdf to Figure_3.pdf and overwriting the original.
files_to_rename.sort(key=lambda f: f['number'], reverse=True)

if not files_to_rename:
    print("🤷 No files found with the 'Figure_<n>' format.")
else:
    print(f"✅ Found {len(files_to_rename)} files to rename. Starting process...\n")
    # Now, iterate through the sorted list and rename
    for file_info in files_to_rename:
        old_path = file_info['path']
        new_number = file_info['number'] + 1
        new_name = f"Figure_{new_number}.{file_info['extension']}"
        new_path = old_path.with_name(new_name)
        
        try:
            old_path.rename(new_path)
            print(f"  {old_path.name}  ->  {new_name}")
        except OSError as e:
            print(f"❌ Error renaming {old_path.name}: {e}")
            
    print("\n🎉 Renaming complete!")

# %%'

    # 🔍 Scanning folder: V:\Labor (VT)\AG Tolba (VT)\P067 NTx Schwein\Results\plots_manuscript\2025-9-17__SEM
    
    # ✅ Found 21 files to rename. Starting process...
    
    #   Figure_7.eps  ->  Figure_8.eps
    #   Figure_7.pdf  ->  Figure_8.pdf
    #   Figure_7.svg  ->  Figure_8.svg
    #   Figure_6.eps  ->  Figure_7.eps
    #   Figure_6.pdf  ->  Figure_7.pdf
    #   Figure_6.svg  ->  Figure_7.svg
    #   Figure_5.eps  ->  Figure_6.eps
    #   Figure_5.pdf  ->  Figure_6.pdf
    #   Figure_5.svg  ->  Figure_6.svg
    #   Figure_4.eps  ->  Figure_5.eps
    #   Figure_4.pdf  ->  Figure_5.pdf
    #   Figure_4.svg  ->  Figure_5.svg
    #   Figure_3.eps  ->  Figure_4.eps
    #   Figure_3.pdf  ->  Figure_4.pdf
    #   Figure_3.svg  ->  Figure_4.svg
    #   Figure_2.eps  ->  Figure_3.eps
    #   Figure_2.pdf  ->  Figure_3.pdf
    #   Figure_2.svg  ->  Figure_3.svg
    #   Figure_1.eps  ->  Figure_2.eps
    #   Figure_1.pdf  ->  Figure_2.pdf
    #   Figure_1.svg  ->  Figure_2.svg
    
    # 🎉 Renaming complete!

# %% manual cropping of images

'''
    everything was done manually here.
    this step is a prerequisite of the next step.
    initially, the whole folder : F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\first_frame_2 : 
        was copied as : F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\first_frame_3
    many images have the same dimension, hence subfolders named : same_n : were createed in each folder to host those images.
    inside each 'same' folder, one of the files was copied as 'sample' ; this file was cropped to contain 14 tiles !


'''

# %% height ( pixel )

'''
    following the previous step, the height of each 'sample' file is extracted & assigned to every other file in the same directory.
    this result is saved in a pandas dataframe containing 2 columns : file_name & height
    a 3rd column mentioning the parent folder where each file existin was also created.

'''

# %%'

import pandas as pd
import cv2  # Use OpenCV instead of Pillow
from pathlib import Path

# %%'

# --- Configuration ---
# Set the root folder you want to search
root_folder = Path(r"F:\OneDrive - Uniklinik RWTH Aachen\VISION\track\first_frame_3")

# --- Script Logic ---

# This list will store our data before we create the DataFrame
data_for_df = []

print(f"🚀 Scanning for 'sample.png' files in: {root_folder}")

# 1. Recursively find all files named 'sample.png'
sample_png_files = list(root_folder.rglob("sample.png"))

if not sample_png_files:
    print("🤷 No 'sample.png' files were found in the specified directory.")
else:
    print(f"✅ Found {len(sample_png_files)} instance(s) of 'sample.png'. Processing...\n")
    
    # 2. Loop through each 'sample.png' that was found
    for sample_path in sample_png_files:
        parent_directory = sample_path.parent
        
        try:
            # 3. Read the image using OpenCV
            # We convert the Path object to a string for cv2.imread()
            image = cv2.imread(str(sample_path))
            
            # Check if the image was loaded successfully
            if image is not None:
                # For OpenCV, the .shape attribute returns (height, width, channels)
                height = image.shape[0]
                
                print(f"Processing folder: {parent_directory}")
                print(f"  -> 'sample.png' height is {height} pixels.")
                
                # 4. Find all other files in the same directory
                sibling_files_found = 0
                for item in parent_directory.iterdir():
                    # Check if it's a file AND not the 'sample.png' file itself
                    if item.is_file() and item.name != "sample.png":
                        # 5. Add a record for this file to our data list
                        data_for_df.append({
                            "file_name": item.name,
                            "sample_png_height": height,
                            "folder_path": parent_directory # Added for extra context
                        })
                        sibling_files_found += 1
                
                if sibling_files_found == 0:
                    print("  -> No other files found in this folder.")
                print("-" * 20)
            else:
                print(f"❌ Error: OpenCV could not load the image at {sample_path}")
                print("-" * 20)

        except Exception as e:
            print(f"❌ An unexpected error occurred with {sample_path}: {e}")

    # 6. Create the final pandas DataFrame from the collected data
    if data_for_df:
        df = pd.DataFrame(data_for_df)
        
        print("\n🎉 Analysis Complete! Here is the resulting DataFrame:\n")
        print(df)

        # Optional: Save the DataFrame to a CSV file
        output_csv_path = root_folder / "image_height_analysis_opencv.csv"
        df.to_csv(output_csv_path, index=False)
        print(f"\n📄 DataFrame also saved to: {output_csv_path}")
    else:
        print("\nNo data was generated. This could be because no other files were found alongside 'sample.png'.")


# %%'

df.shape
# Out[3]: (111, 3)


df[:4]
    # Out[4]: 
    #         file_name  ...                                        folder_path
    # 0  pod_1_ZC14.png  ...  F:\OneDrive - Uniklinik RWTH Aachen\VISION\tra...
    # 1  pod_3_ZC14.png  ...  F:\OneDrive - Uniklinik RWTH Aachen\VISION\tra...
    # 2  pod_4_ZC14.png  ...  F:\OneDrive - Uniklinik RWTH Aachen\VISION\tra...
    # 3  pod_7_ZC14.png  ...  F:\OneDrive - Uniklinik RWTH Aachen\VISION\tra...
    
    # [4 rows x 3 columns]

df.iloc[:4 , :2]
    # Out[5]: 
    #         file_name  sample_png_height
    # 0  pod_1_ZC14.png                569
    # 1  pod_3_ZC14.png                569
    # 2  pod_4_ZC14.png                569
    # 3  pod_7_ZC14.png                569

df.iloc[-4: , :2]
    # Out[6]: 
    #           file_name  sample_png_height
    # 107  pod_1_ZC08.png                564
    # 108  pod_1_ZC09.png                564
    # 109  pod_1_ZC10.png                564
    # 110  pod_1_ZC11.png                564

df.iloc[:4 , 2 ]

# %%'


# %%'

