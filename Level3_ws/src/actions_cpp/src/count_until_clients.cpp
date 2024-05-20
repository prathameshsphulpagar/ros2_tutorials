#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"
#include "my_robot_interfaces/action/count_until.hpp"

using CountUntil = my_robot_interfaces::action::CountUntil;
class CountUntilClientsNode : public rclcpp::Node // MODIFY NAME
{
public:
    CountUntilClientsNode() : Node("CountUntilClientsNode") // MODIFY NAME
    {
        count_until_client_ = rclcpp_action::create_client<CountUntil>(this,"count_until");
    }

    void send_goal(int target_number,double period)
    {
         // send the value to the client node.
        count_until_client_->wait_for_action_server();

        auto goal = Countntil::Goal();
        goal.target_number = target_number;
        goal.period = period;
    }
private:
    rclcpp_action::Client<CountUntil>::SharedPtr count_until_client_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<CountUntilClientsNode>(); // MODIFY NAME
    node->send_goal(6, 0.8);
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}