
def expanding_window_splits(
    observations,
    minimum_train_size=40,
    horizon=1
):

    n = len(observations)

    if minimum_train_size < 1 or horizon < 1:
        raise ValueError("Invalid window configuration")

    if minimum_train_size + horizon > n:
        raise ValueError("Insufficient observations")

    splits = []

    for end in range(
        minimum_train_size,
        n - horizon + 1
    ):

        train = observations[:end]

        test = observations[
            end:end + horizon
        ]

        splits.append((train, test))

    return splits
