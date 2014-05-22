library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ClockGenerator is
	generic(
		count : natural := 50000000
	);
	port(
		clk : in std_logic;
		rst : in std_logic;
		q   : out std_logic
	);
end entity ClockGenerator;

architecture RTL of ClockGenerator is
begin
	process(clk, rst)
		variable value : integer range 0 to count := 0;
	begin
		if (rst = '0') then
			value := 0;
		elsif (clk'event) and (clk = '1') then
			value := value + 1;
		end if;

		if (value = count) then
			value := 0;
			q <= '1';
		else
			q <= '0';
		end if;
	end process;
end architecture RTL;
