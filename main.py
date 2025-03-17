import pandas as pd

#####################
# YOU MUST WRITE YOUR STUDENT ID IN THE VARIABLE STUDENT_ID
# EXAMPLE: STUDENT_ID = "12345678"
#####################
STUDENT_ID = "12345678"

def load_data():
    # EXAMPLE
    # Load the data from a csv file
    # You can change function
    train = pd.read_csv('./data/redwine_train.csv')
    test = pd.read_csv('./data/redwine_test.csv')

    return train, test

def save_data(df1, df2):
    # EXAMPLE
    # Save the data to a csv file
    # You can change function
    # BUT you should keep the file name as "{STUDENT_ID}_simple_seq.answer.csv"
    df1.to_csv(f'{STUDENT_ID}_simple_seq.p1.answer.csv')
    df2.to_csv(f'{STUDENT_ID}_simple_seq.p2.answer.csv')

def main():
    # WRITE YOUR CODE HERE
    save_data(df)

if __name__ == "__main__":
    main()