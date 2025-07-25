
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
directory = r'D:\video\pod_1'
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
    # as it needs user input ( defining the edges of a curved side ), this can not be dne fully automated !!

# Define the input directory
# uw : un-warp
input_dir = r'D:\video\pod_1'
output_dir = os.path.join(input_dir, 'uw')

# Ensure the output directory exists
# os.makedirs(output_dir, exist_ok=True)

# Iterate over files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.mp4'):  # Check if the file is an .mp4 video
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename.replace('.mp4', '_uw.mp4'))
        command = f'python undistort.py {input_path} {output_path} --balance 0.3'
        print(command)


# %%'  retrain_2 commands

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

# %%' pod_1 commands

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

# %% histogram equalization : multile files

# this automates running the sub-process for multiple files.
    # since unlike the unwarping, there is no user input !
        # hence, it can run un-supervised !
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
input_dir   = Path(r'D:\video\pod_1\uw\low_light')
output_dir  = Path(r'D:\video\pod_1\uw\equalized')
script_path = Path(r'U:\VISION\track\pre-process\histogram_equalization.py')
ext         = '.mp4'


# === Prepare output directory ===
output_dir.mkdir(parents=True, exist_ok=True)


# === Loop through videos ===
for video_path in input_dir.glob(f'*{ext}'):
    out_path = output_dir / video_path.name
    print(f'Processing: {video_path.name}')
    subprocess.run([
        'python',
        str(script_path),
        str(video_path),
        str(out_path)
    ], check=True)

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

# %% create a folder for each video file.

from pathlib import Path
import shutil

# %%'

# 1) Configure your input directory
input_dir = Path(r"D:\video\pod_1\uw\equalized")

# 2) Loop over every .mp4 file
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

# %% extract the 1st frame

# this presuably extracts the 1st frames from all videos in a directory.
# this was probably done to then calculate the pixel-meter length conversion.
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

# %%'


