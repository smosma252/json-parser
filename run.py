import ReadFile
import ProcessData


def process_data():
    """
    Reads, parses and console logs data with matching tags
    :return: Prints data with matching tags.
    """

    # Parses through the data
    users_data = ReadFile.parse_json("data/users.json")
    jobs_data = ReadFile.parse_json("data/jobs.json")

    # Matches the user tags with job tags.
    if users_data is None or jobs_data is None:
        print("File has not parsed correctly.")
    else:
        # Prints the data with matching tags
        ProcessData.tag_matcher(users_data, jobs_data)

if __name__ == '__main__':
    process_data()
