def get_job_tags_and_id(jobs_data: list):
    """
    Refactors the data by creating a dictionary with keys as the job id and values as a set of job tags.
    :param jobs_data: List of objects containing job details
    :return: Dictionary with keys as id and list of job_tags as value
    """

    job_tags = {}
    for job in jobs_data:
        id_number = job['id']
        job_tags[id_number] = set(job['tags'])  # Convert values to sets for quick search
    return job_tags


def tag_matcher(user_data, jobs_data):
    """
    Matches the users tags with the jobs tags. If we find at least two matching user tags in job tags we print.
    Those that are matching.
    :param user_data: List of objects containing user data
    :param jobs_data: List of objects containing job data
    :return: prints statement matching users tags with jobs tags
    """

    # Gets refactored jobs data
    job_tags = get_job_tags_and_id(jobs_data)

    # Loops through users
    for user in user_data:
        user_tags = user['tags']

        # Loops through jobs
        for job in job_tags:
            set_of_job_tags = job_tags[job]

            user_tag_counter = 0

            # Loops through user tags
            for tag in user_tags:

                # Checks to see if the current user tag is in job tag
                if tag in set_of_job_tags:
                    user_tag_counter += 1

                # If we have found at least 2 tags we can stop
                if user_tag_counter >= 2:
                    user_id = user['id']
                    print("user " + str(user_id) + ": matches to " + str(jobs_data[job - 1]))
                    break
