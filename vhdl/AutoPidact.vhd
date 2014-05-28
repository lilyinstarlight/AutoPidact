library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity AutoPidact is
	port(
		CLOCK_50_B5B : in    std_logic;
		GPIO         : inout std_logic_vector(35 downto 0);
		LEDR         : out   std_logic_vector(9 downto 0)
	);
end entity AutoPidact;

architecture RTL of AutoPidact is
	signal mtr0_pwm : unsigned(2 downto 0);
	signal mtr0     : std_logic;
	signal mtr1_pwm : unsigned(2 downto 0);
	signal mtr1     : std_logic;
	signal mtr2_pwm : unsigned(2 downto 0);
	signal mtr2     : std_logic;
	signal mtr3_pwm : unsigned(0 downto 0);
	signal mtr3     : std_logic;
begin
	mtr0_pwm <= unsigned(GPIO(9 downto 7));
	mtr1_pwm <= unsigned(GPIO(12 downto 10));
	mtr2_pwm <= unsigned(GPIO(15 downto 13));
	mtr3_pwm <= unsigned(GPIO(16 downto 16));

	pwm0: entity work.PWM
	      generic map(cycle => 500000, width => 7)
	      port map(clk => CLOCK_50_B5B, pwm => mtr0_pwm, q => mtr0);

	pwm1: entity work.PWM
	      generic map(cycle => 500000, width => 7)
	      port map(clk => CLOCK_50_B5B, pwm => mtr1_pwm, q => mtr1);

	pwm2: entity work.PWM
	      generic map(cycle => 500000, width => 7)
	      port map(clk => CLOCK_50_B5B, pwm => mtr2_pwm, q => mtr2);

	pwm3: entity work.PWM
	      generic map(cycle => 500000, width => 1)
	      port map(clk => CLOCK_50_B5B, pwm => mtr3_pwm, q => mtr3);

	GPIO(3) <= mtr0;
	GPIO(4) <= mtr1;
	GPIO(5) <= mtr2;
	GPIO(6) <= mtr3;
end RTL;