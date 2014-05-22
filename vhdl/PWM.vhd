library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity PWM is
	generic(
		cycle : natural := 50000;
		width : natural := 255
	);
	port(
		clk : in  std_logic;
		pwm : in  unsigned;
		q   : out std_logic
	);
end entity PWM;

architecture RTL of PWM is
	signal clock : std_logic := '1';
begin
	cg0: entity work.ClockGenerator
	     generic map(count => cycle)
	     port map(clk => clk, rst => '1', q => clock);

	process(clock, pwm)
		variable value : integer range 0 to width := 0;
	begin
		if (clock'event) and (clock = '1') then
			value := value + 1;
		end if;

		if (value > width) then
			value := 0;
		end if;

		if (value >= pwm) then
			q <= '0';
		else
			q <= '1';
		end if;
	end process;
end RTL;
