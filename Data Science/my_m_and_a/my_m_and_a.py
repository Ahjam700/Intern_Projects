import pandas as pd

def my_m_and_a(content_database_1, content_database_2, content_database_3):
    #  CSV file
    try:
        df1 = pd.read_csv(content_database_1)
        df2 = pd.read_csv(content_database_2)
        df3 = pd.read_csv(content_database_3)
    except FileNotFoundError as e:
        raise ValueError(f"One or more CSV files not found: {e}")

    # remove duplicates
    merged_df = pd.concat([df1, df2, df3], ignore_index=True).drop_duplicates()

    # our column names
    my_columns = {
        "firstname": "FirstName",
        "lastname": "LastName",
        "age": "Age", 
        "gender": "Gender",
        "city": "City",
        "country": "Country",
        "created_at": "CreatedAt",
        "referral": "Referral",
    }
    merged_df.rename(columns={k.lower(): v for k, v in my_columns.items()}, inplace=True)

    merged_df.drop(columns=["Name", "name"], errors="ignore", inplace=True)

    columns_to_convert = ["Gender", "FirstName", "LastName", "Email", "Age", "City", "Country", "CreatedAt", "Referral"]
    for column in columns_to_convert:
        if column in merged_df.columns:
            merged_df[column] = merged_df[column].astype(str)

    # capitalize city names
    if "City" in merged_df.columns:
        merged_df["City"] = merged_df["City"].str.title()


    #   gender column
    if "Gender" in merged_df.columns:
        valid_genders = {"female": "Female", "male": "Male"}
        merged_df["Gender"] = merged_df["Gender"].str.lower().map(valid_genders)
        merged_df = merged_df[merged_df["Gender"].isin(["Female", "Male"])]

    #  Age values are strings
    if "Age" in merged_df.columns:
        merged_df["Age"] = merged_df["Age"].apply(lambda x: str(x).strip() if pd.notna(x) else "")

    for col in ["FirstName", "LastName"]:
        if col in merged_df.columns:
            merged_df[col] = merged_df[col].str.title().str.strip()
            merged_df[col] = merged_df[col].apply(lambda x: "" if "string_" in x.lower() else x)

    # handling missing values
    merged_df.fillna({"FirstName": "", "LastName": "", "Age": "", "City": "", "Gender": "Unknown"}, inplace=True)
    return merged_df
