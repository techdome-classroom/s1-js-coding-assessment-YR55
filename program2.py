def is_match(message, key):
    def match_helper(message, key):
        # If both message and key are exhausted
        if not message and not key:
            return True
        # If key is exhausted but message is not, or vice versa
        if not key and message:
            return False
        if not message and key:
            # Star symbol can replace any sequence (including none)
            return key == '*'
        
        # Handle star symbol '*' in key
        if key[0] == '*':
            # The '*' can replace any sequence of letters (including none)
            # Try to match the rest of the key with progressively smaller slices of the message
            return match_helper(message, key[1:]) or (message and match_helper(message[1:], key))
        
        # Handle question mark '?' in key
        if key[0] == '?':
            # '?' matches exactly one letter, so consume one letter from the message and continue
            return message and match_helper(message[1:], key[1:])
        
        # Regular character match
        if key[0] == message[0]:
            return match_helper(message[1:], key[1:])
        
        # If none of the conditions match
        return False
    
    return match_helper(message, key)

# Test cases from the problem
print(is_match("aa", "a"))      # False
print(is_match("aa", "a*"))     # True
print(is_match("cb", "?a"))     # False