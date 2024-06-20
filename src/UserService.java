interface UserRepository {
    User findUserById(String id);
}

public class UserService {
    private UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public String getUserName(String id) {
        User user = userRepository.findUserById(id);
        return (user != null) ? user.getName() : "Unknown";
    }
}
 class User {
    private String id;
    private String name;

    public User(String id, String name) {
        this.id = id;
        this.name = name;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}