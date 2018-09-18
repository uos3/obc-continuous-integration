Toolchain designed for automated and remote testing of each change to obc software. Each time you a new commit is detected to a specified branch in the config, an attempt to compile it will be made, if successful, a test on the physical microcontroller will proceed. The outcome of all actions are logged, kept, and returned back to the user responsible for the commit.

Designed to be used for Linux, and run on the ground station server.

Back-end (Linux)
Git API -> Server-side compilation -> Flash to TOBC -> Outputs sent to front-end

Front-end
Email (uos3bot@gmail.com)

Install process
-Clone uos3/continous-integration
-Add logs folder
-Add config.py with EMAIL, EMAIL_TARGET, and EMAIL_PASSWORD for the CubeBot to front-end/
-Clone uos3/obc-firmware and follow standard procedures on that README
-Connect up physical hardware