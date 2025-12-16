def calculate_pyramid_height(number_of_blocks: int) -> int:
    """
    Calculate pyramid height from number of blocks.
    Pyramid structure: 1 + 2 + 3 + ... + height = number_of_blocks
    """
    height = 0
    total_blocks = 0
    
    while total_blocks < number_of_blocks:
        height += 1
        total_blocks += height
    
    if total_blocks == number_of_blocks:
        return height
    else:
        return height - 1