import { useEffect, useState } from 'react'
import './Header.scss'
import HeaderDesktop from './HeaderDesktop'
import HeaderMobile from './HeaderMobile'

function Header() {
	const [width, setWidth] = useState(window.innerWidth)

	useEffect(() => {
		const handleResize = () => {
			setWidth(window.innerWidth)
		}

		window.addEventListener('resize', handleResize)

		return () => {
			window.removeEventListener('resize', handleResize)
		}
	}, [])

	return <header>{width >= 992 ? <HeaderDesktop /> : <HeaderMobile />}</header>
}

export default Header
